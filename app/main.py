from news_fetcher import NewsFetcher
from topic_extractor import TopicExtractor
from news_filter import NewsFilter
from storage import Storage

if __name__ == '__main__':
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

    # Filter topics
    filter = NewsFilter('data/topics.json')
    filtered_by_keyword = filter.filter_by_keyword('israel')
    Storage.save_to_file(filtered_by_keyword, 'data/filtered_by_keyword.json')
    print("Filtered by keyword and stored in data/filtered_by_keyword.json")
    filtered_by_date = filter.filter_by_date('2024-10-04', '2024-10-04')
    Storage.save_to_file(filtered_by_date, 'data/filtered_by_date.json')
    print("Filtered by date and stored in data/filtered_by_date.json")
