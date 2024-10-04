import json
import os

class Storage:
    """
    A utility class for saving and loading data to/from JSON files.
    """

    @staticmethod
    def save_to_file(data, file_path):
        """
        Save data to a JSON file.

        Args:
            data: The data to be saved (must be JSON serializable).
            file_path (str): The path to the file where data will be saved.

        Returns:
            None
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(file_path):
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the file to load data from.

        Returns:
            The data loaded from the JSON file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"File not found: {file_path}")


