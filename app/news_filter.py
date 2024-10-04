from storage import Storage
import json
from datetime import datetime

class NewsFilter:
    """
    A class for filtering news articles based on keywords and dates.

    Attributes:
        json_file_path (str): The path to the JSON file containing news articles.
    """

    def __init__(self, json_file_path):
        """
        Initialize the NewsFilter with a JSON file path.

        Args:
            json_file_path (str): The path to the JSON file containing news articles.
        """
        self.json_file_path = json_file_path

    def filter_by_keyword(self, keyword):
        """
        Filter articles based on a given keyword.

        Args:
            keyword (str): The keyword to filter articles by.

        Returns:
            list: A list of articles containing the keyword in their description.

        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the JSON file has an invalid format.
            Exception: For any other unexpected errors.
        """
        try:
            articles = Storage.load_from_file(self.json_file_path)
            filtered = [article for article in articles if keyword.lower() in article['description'].lower()]
            return filtered
        except FileNotFoundError:
            print(f"Error: File '{self.json_file_path}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file '{self.json_file_path}'.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return []

    def filter_by_date(self, start_date, end_date):
        """
        Filter articles based on a date range.

        Args:
            start_date (str): The start date in 'YYYY-MM-DD' format.
            end_date (str): The end date in 'YYYY-MM-DD' format.

        Returns:
            list: A list of articles published within the specified date range.

        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the JSON file has an invalid format.
            ValueError: If the date format is invalid.
            Exception: For any other unexpected errors.
        """
        try:
            articles = Storage.load_from_file(self.json_file_path)
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            filtered = [
                article for article in articles
                if start_date <= datetime.strptime(article['published'], '%a, %d %b %Y %H:%M:%S %Z').date() <= end_date
            ]
            return filtered
        except FileNotFoundError:
            print(f"Error: File '{self.json_file_path}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file '{self.json_file_path}'.")
            return []
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return []