# Amazon Bedrock News Summarizer

Amazon bedrock project demonstrates how to add function calling news data source from the web and integrating with Amazon Bedrock. The code fetch news from multiple RSS feeds, APIs and utilize Amazon Bedrock to process and generate list of news and summary based on the fetched news data. It integrates news data from RSS feeds from Cointelegraph, GNews and NewsAPI, formats it, and sends it to an Amazon Bedrock Anthropic Claude models(interchangeable) for summary of list of latest  news.

## Features

- **News Data Retrieval**: Fetch news from the RSS feeds, GNews and NewsAPI services. You can add or remove RSS feeds and APIs based on your requirememnts.
- **Amazon Bedrock Integration**: Use Amazon Bedrock to invoke a machine learning model that processes news data.
- **Modular Design**: Easily extendable for additional news sources like RSS feeds, news Apis by implementing a base news fetcher class.

## Overview

This news summarization tool leverages Amazon Bedrock's powerful language models to fetch and condense news articles. It utilizes a flexible framework that can integrate multiple news sources, including GNews, NewsAPI, and RSS feeds. This system is designed to be easily expandable, allowing for the seamless addition of new sources.
The tool's core is a base class called NewsFetcher, which defines a standard way for subclasses to retrieve and format news data from various APIs and RSS feeds.  This modular approach ensures the code is maintainable and adaptable as new sources are added.
By combining this fetched news data, the tool harnesses the capabilities of Amazon Bedrock's language models, effectively summarizing the most relevant information into concise summaries. This streamlined process is facilitated by libraries like boto3, langchain, and langchain-aws, resulting in a powerful and efficient news summarization solution.


## Setup

### Prerequisites

- Python 3.6 or higher
- Boto3
- urllib
- NewsAPI Python Client
- AWS CLI configured with appropriate AWS credentials
- langchain
- langchain-aws

### Python Libraries
To run the news-summarizer script, you will need to install several Python libraries. These include:

boto3: AWS SDK for Python, used for interacting with AWS services including AWS Bedrock.
urllib.request: A module for opening URLs, used to fetch news data from the GNews API.
NewsAPI Python Client: A client library to fetch news from NewsAPI.
You can install these libraries using pip:

```
pip install boto3 newsapi-python
```
### AWS Configuration and Credentials
Before you can interact with AWS services through boto3, you need to configure your AWS credentials:

AWS CLI Installation: First, ensure that AWS CLI is installed on your system.

```
pip install awscli
```
 Install the libraries for news-api
```
pip install newsapi-python
```
### Configure AWS CLI: Set up your AWS credentials (AWS Access Key ID and AWS Secret Access Key) and default region using the AWS CLI. These credentials should be associated with an AWS account that has permissions to access the required AWS services.

```
aws configure
```

### AWS IAM Roles and Permissions
Create a user with administrative access and secure your AWS account root user by enabling multi-factor authentication. Finally, request access to the desired Amazon Bedrock models through the AWS Management Console, ensuring all API and user permissions are properly configured for compliance and operational needs.

#### Sample IAM Role for Amazon Bedrock Usage:
Here's an example of an IAM role JSON policy document that grants necessary permissions to use Amazon Bedrock, specifically tailored for allowing the invocation of models and managing API interactions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockModelInvoke",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*:123456789012:model/*"
            ]
        },
        {
            "Sid": "ManageAPIInteractions",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetModel",
                "bedrock:ListModelVersions",
                "bedrock:ListModels"
            ],
            "Resource": "*"
        }
    ]
}

```

### Environment Variables
Set environment variables for the API keys needed for GNews and NewsAPI, ensuring they are securely stored  in the enviroment or in AWS Secrets Manager and accessible in your development environment:

```
export GNEWS_API_KEY='your_gnews_api_key_here'
export NEWS_API_KEY='your_news_api_key_here'
```

6. Security Considerations
Make sure that your script and environment adhere to best security practices, such as not hardcoding sensitive information (like API keys and AWS credentials) directly in the script. Use environment variables or secure vaults like AWS Secrets Manager for handling sensitive data.


## Note
You will have to subscribe news-api and gnews api to use this code. 















