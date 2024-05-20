
import urllib.request
from newsapi import NewsApiClient
import json
import feedparser

class NewsFetcher:
    """
    Base class for fetching news. Subclasses must implement fetch_news method.
    """
    def fetch_news(self, query, max_articles):
        raise NotImplementedError("Subclasses must implement this method.")

class GNewsFetcher(NewsFetcher):
    def __init__(self, api_key=None):  # Allow initialization without an API key
        self.api_key = api_key

    def fetch_news(self, query, max_articles=5):
        if self.api_key:
            url = f"https://gnews.io/api/v4/search?q={query}&max=10&apikey={self.api_key}"
            articles_list = []
            try:
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]
                    for article in articles[:max_articles]:
                        articles_list.append(f"{article['title']}, {article['description']}, {article['url']}")
            except Exception as e:
                print(f"An error occurred fetching GNews: {e}")
            return articles_list
        else:
            print("GNews API key is missing. Skipping...")
            return []  # Return an empty list if no API key

class NewsAPIFetcher(NewsFetcher):
    def __init__(self, api_key=None):  # Allow initialization without an API key
        self.api_key = api_key
        if self.api_key:  # Only initialize the client if the key is provided
            try:
                self.newsapi_client = NewsApiClient(api_key=api_key)
            except Exception as e:
                print(f"NewsAPI initialization failed: {e}. Skipping...")
                self.newsapi_client = None
        else:
            self.newsapi_client = None

    def fetch_news(self, query, max_articles=5):
        if self.newsapi_client:  # Fetch only if the client was initialized
            try:
                top_news = self.newsapi_client.get_everything(
                    q=query, language='en', sort_by='relevancy', page_size=max_articles
                )
                articles_list = []
                for article in top_news['articles']:
                    articles_list.append(f"{article['title']}, {article['description']}, {article['url']}")
                return articles_list
            except Exception as e:
                print(f"An error occurred fetching NewsAPI: {e}")
        
        # If the client wasn't initialized or fetching failed, return an empty list
        print("NewsAPI key is missing or invalid. Skipping...")
        return []

class RSSFeedFetcher(NewsFetcher):
    def __init__(self, feed_url):
        self.feed_url = feed_url

    def fetch_news(self, query, max_articles=5):  
        """Fetches news from a given RSS feed URL."""
        feed = feedparser.parse(self.feed_url)
        articles_list = []

        for entry in feed.entries[:max_articles]:
            title = entry.get("title")
            description = entry.get("description")
            url = entry.get("link")
            articles_list.append(f"{title}, {description}, {url}")

        return articles_list