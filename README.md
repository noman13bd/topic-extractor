# News Aggregator with Topic Extraction

This is a Python-based news aggregator application that fetches articles from configurable RSS feeds, performs topic and named entity extraction using SpaCy, and allows filtering by keywords or publication date. The project is containerized using Docker Compose, enabling both manual and automated operations (via a scheduler) for continuous data fetching.

## Features

1. RSS Feed Fetching: Pulls news articles from configurable RSS feed URLs.
2. Topic Extraction: Extracts topics and named entities (people, locations, organizations) from the articles using SpaCy.
3. Filtering: Supports filtering of articles based on keywords and publication date.
4. Persistence: Stores articles and their topics in JSON files.
5. Scheduler: Automatically fetches news articles every hour.
6. Containerized Setup: Runs using Docker Compose for easy setup and deployment.

## Prerequisites

- Docker and Docker Compose installed.
- Python 3.9+ (if running outside Docker).
- SpaCy model: The project uses SpaCy for named entity recognition, so the en_core_web_sm model should be downloaded.

## Setup Instructions

1. Clone the repository:
     ```
     git clone git@github.com:noman13bd/topic-extractor.git
     cd topic-extractor
    ```

2. Update RSS feed URLs:

     Modify the list of RSS feed URLs in `app/main.py` & `app/scheduler.py` to include your preferred news sources.
   

## Usage

### 1. Running the Scheduler (for Automatic Hourly Fetching)

The scheduler fetches articles every hour and processes them automatically. Use the following command to start the scheduler:

`docker compose run scheduler`

The scheduler will:
- Fetch articles from the configured RSS feeds.
- Extract topics and named entities using SpaCy.
- Save the results in `data/articles.json` and `data/topics.json`.

### 2. Running the Main Application Manually (for Filtering)

You can run the application manually to fetch and filter data at any time. To do so:

`docker compose run news_aggregator`

This will:

- Fetch and process articles.
- Save the results to `data/articles.json` and `data/topics.json`.
- Perform filtering and save the filtered data based on keywords or date to separate files (`filtered_by_keyword.json` and `filtered_by_date.json`).

### 3. Filtering by Keywords or Date

Once articles and topics are saved, you can filter them using the criteria you choose.

- Filter by Keyword: Searches for articles containing the specified keyword.
    - Filtered data will be saved in `data/filtered_by_keyword.json`.

- Filter by Date: Filters articles based on a date range.
    - Filtered data will be saved in `data/filtered_by_date.json`.

## Logs and Monitoring

- Scheduler Logs: To check the logs of the scheduler (for any issues in fetching or processing), run:
  
    `docker logs scheduler`
  
- News Aggregator Logs: To view the logs of a manual run of `main.py`, use:
  
    `docker logs news_aggregator`
  
## Example Output

The data fetched and processed by the news aggregator is saved in the `data` folder as JSON files:

- `data/articles.json`: Contains the raw articles with metadata like title, description, and publication date.
- `data/topics.json`: Includes extracted topics and named entities for each article.
- `data/filtered_by_keyword.json`: Contains articles filtered by the provided keyword.
- `data/filtered_by_date.json`: Contains articles filtered by the provided date range.

## Dependencies

- Python 3.9+
- Libraries:
    - feedparser
    - spacy
    - schedule
- SpaCy Model:
    - en_core_web_sm