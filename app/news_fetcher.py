from storage import Storage
import feedparser
import json
import os
from datetime import datetime

class NewsFetcher:
    """
    A class for fetching news articles from RSS feeds.

    Attributes:
        rss_urls (list): A list of RSS feed URLs to fetch articles from.
    """

    def __init__(self, rss_urls):
        """
        Initialize the NewsFetcher with a list of RSS feed URLs.

        Args:
            rss_urls (list): A list of RSS feed URLs.
        """
        self.rss_urls = rss_urls

    def fetch_articles(self):
        """
        Fetch articles from the RSS feeds.

        Returns:
            list: A list of dictionaries containing article information.
        """
        articles = []
        for url in self.rss_urls:
            try:
                print(f"Fetching data from {url}...")
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    articles.append({
                        "title": entry.title,
                        "description": entry.description,
                        "published": entry.published if hasattr(entry, 'published') else str(datetime.now()),
                        "source_url": entry.link
                    })
            except Exception as e:
                print(f"Error fetching data from {url}: {str(e)}")
        return articles

    def save_to_json(self, data, file_path):
        """
        Save the fetched data to a JSON file.

        Args:
            data: The data to be saved.
            file_path (str): The path to the file where the data will be saved.
        """
        Storage.save_to_file(data, file_path)
