import requests
import os
import json
import boto3
from langchain.tools import tool, StructuredTool
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import Bedrock
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
#from langchain_community.chat_models import BedrockChat

# Assuming you have 'news_fetchers.py' with the fetch_all_news function 
from news_fetchers import GNewsFetcher, NewsAPIFetcher,RSSFeedFetcher



ModelId="anthropic.claude-3-sonnet-20240229-v1:0"
GNEWS_API_KEY = ""
NEWS_API_KEY = ""

def invoke_bedrock_for_summary(prompt_text: str) -> str:
    """Invokes Bedrock to generate a news summary from the given prompt text."""
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    # Format the prompt as a single string
    prompt = f"""
    Human: You are a helpful assistant who extracts news articles.
    Human: From the following news data, extract the 3 latest Bitcoin news, each with a headline, brief summary, and URL.
    {prompt_text}
    Assistant:
     """ 

    body = json.dumps({"prompt": prompt, "max_tokens_to_sample": 4096, "temperature": 0.5, "top_k": 250, "top_p": 0.5, "stop_sequences": []})

    # Use InvokeModelWithResponseStream API
    response = bedrock.invoke_model(
        body=body, 
        modelId=ModelId, 
        accept='application/json', 
        contentType='application/json'
    )

    response_body = ""
    for event in response['body']:
        response_body += event["chunk"]["bytes"].decode("utf-8")
    return json.loads(response_body).get("completion")

    
def fetch_all_news(news_sources, query, max_articles):
    """
    Fetch news from all configured news sources.
    
    Args:
        news_sources (list): A list of NewsFetcher instances.
        query (str): The search query for fetching news.
        max_articles (int): The maximum number of articles per source.
        
    Returns:
        list: A list containing combined news articles from all sources.
    """
    combined_articles = []
    for source in news_sources:
        combined_articles.extend(source.fetch_news(query, max_articles))
        
    
    return combined_articles
    
@tool("get_news_summary")
def get_news_summary(query: str, max_articles_per_source: int = 3) -> str:
    """Fetches news from multiple sources and returns a summarized version."""
    
    # Load API keys (ensure these are set as environment variables)
    

    news_sources = [
    GNewsFetcher(GNEWS_API_KEY), 
    NewsAPIFetcher(NEWS_API_KEY),
    RSSFeedFetcher("https://cointelegraph.com/rss/tag/bitcoin"),  # Cointelegraph
    RSSFeedFetcher("https://bitcoinmagazine.com/.rss/full/")  # Add more RSS feeds here
    ]
    combined_news = fetch_all_news(news_sources, query, max_articles_per_source)

    prompt_text = f"Human: Extract the news in 2 liners with title and description, and provide URLs as references" + str(combined_news) + "\nAssistant:"

    # Bedrock invocation using boto3
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    prompt_params = {
        "prompt": prompt_text,
        "max_tokens_to_sample": 4096,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": []
    }
    body = json.dumps(prompt_params).encode('utf-8')
    response = bedrock.invoke_model(body=body, modelId="anthropic.claude-v2", accept='application/json', contentType='application/json')

    return json.loads(response.get('body').read()).get("completion") 



# LangChain Agent Setup
tools_list = [get_news_summary]


# Modified LangChain Agent Setup
bedrock_runtime = boto3.client(service_name='bedrock-runtime')

# Instantiate LLM from Bedrock directly (without BedrockChat)


llm = ChatBedrock(model_id=ModelId, client=bedrock_runtime)

react_agent = initialize_agent(
    tools_list,
    llm,  # Pass the LLM instance
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


# Example Usage
result = react_agent({"input": "  Bitcoin news "})
print(result["output"])
