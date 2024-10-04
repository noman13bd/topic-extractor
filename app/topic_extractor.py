from storage import Storage
import json
import spacy

class TopicExtractor:
    """
    A class for extracting topics and entities from articles stored in a JSON file.

    Attributes:
        json_file_path (str): Path to the JSON file containing articles.
        nlp (spacy.lang): Spacy language model for natural language processing.
    """

    def __init__(self, json_file_path):
        """
        Initialize the TopicExtractor with a JSON file path.

        Args:
            json_file_path (str): Path to the JSON file containing articles.
        """
        self.json_file_path = json_file_path
        self.nlp = spacy.load("en_core_web_sm")

    def extract_topics_and_entities(self):
        """
        Extract topics and named entities from articles in the JSON file.

        Returns:
            list: A list of dictionaries, each containing an article with extracted topics and entities.
        """
        with open(self.json_file_path, 'r') as file:
            articles = json.load(file)

        articles_with_topics = []
        
        for article in articles:
            doc = self.nlp(article['description'])

            # Extract keywords (based on noun chunks as a simple topic extraction technique)
            topics = [chunk.text for chunk in doc.noun_chunks]

            # Extract named entities
            entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

            article['topics'] = topics
            article['entities'] = entities
            articles_with_topics.append(article)

        return articles_with_topics

    def save_topics_to_json(self, topics_data, output_path):
        """
        Save the extracted topics and entities data to a JSON file.

        Args:
            topics_data (list): List of dictionaries containing articles with extracted topics and entities.
            output_path (str): Path to save the output JSON file.
        """
        Storage.save_to_file(topics_data, output_path)
