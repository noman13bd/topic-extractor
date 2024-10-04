import schedule
import time
from news_fetcher import NewsFetcher
from topic_extractor import TopicExtractor
from storage import Storage
from datetime import datetime

def fetch_and_process_articles():
    print("Fetching and processing articles...")
    
    rss_urls = [
        # 'https://www.ajplus.net/stories?format=rss',
        'https://rss.cnn.com/rss/edition_world.rss',
        'https://feeds.bbci.co.uk/news/world/rss.xml'
    ]
    
    # Fetch articles and store them in articles.json
    fetcher = NewsFetcher(rss_urls)
    articles = fetcher.fetch_articles()
    fetcher.save_to_json(articles, 'data/articles.json')
    print("Articles fetched and stored in data/articles.json")

    # Extract topics and entities and store them in topics.json
    extractor = TopicExtractor('data/articles.json')
    articles_with_topics = extractor.extract_topics_and_entities()
    extractor.save_topics_to_json(articles_with_topics, 'data/topics.json')
    print("Topics and entities extracted and stored in data/topics.json")

    print("Articles fetched and processed successfully.")

# Schedule the fetch job to run every hour
schedule.every(1).hours.do(fetch_and_process_articles)

if __name__ == "__main__":
    # Run the scheduled tasks continuously
    print("Starting scheduler...")
    fetch_and_process_articles()  # Fetch once at the start
    while True:
        schedule.run_pending()
        time.sleep(1)
