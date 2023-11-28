# AI Demo Project Using Codeanywhere

## Project Overview

Welcome to our AI Demo Project, showcasing the integration and application of AI technologies in Python with Codeanywhere. This project now includes features for generating articles using OpenAI's API, along with existing functionality for fetching, storing, and searching web content using ChromaDB.

### Main Features:
- **Sitemap Fetching and Parsing**: Automates the process of fetching sitemap XML from websites and parsing it to extract URLs.
- **Content Extraction and Storage**: Retrieves and stores web page content in ChromaDB, a versatile database system.
- **AI-Powered Search**: Employs OpenAI's embedding functions for efficient and intelligent content search within ChromaDB.
- **Article Generation**: Generates articles based on user prompts and search terms, utilizing OpenAI's GPT-4 model.

## Getting Started

### Prerequisites
- Python 3.x
- Access to Codeanywhere or a similar cloud-based development environment.
- OpenAI API key

### Installation
1. Clone the repository to your Codeanywhere container.
2. Install necessary packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up an `.env` file with your `OPENAI_API_KEY`.

### Usage

1. **main.py**: 
   - Run the script with a sitemap URL to fetch, parse, and store website content.
   - Usage: `python main.py [SITEMAP_URL]`

2. **search.py**:
   - Perform searches in the stored data.
   - Usage: `python search.py [SEARCH_QUERY]`

3. **query.py**:
   - Generate articles based on a prompt and ChromaDB search terms.
   - Usage: `python generate_article.py [PROMPT] --s [SEARCH_TERM] --n [NUMBER_OF_RESULTS]`

## Structure

- `main.py`: Main script for fetching and storing website content.
- `search.py`: Script to search within the stored data.
- `query.py`: Script to generate articles using OpenAI and ChromaDB to fetch context.
- `db/`: Directory containing ChromaDB client and utilities.
- `.env`: Environment file for storing your OpenAI API key.

## Examples

- Fetch and store content:
  ```bash
    python main.py https://example.com/sitemap.xml
  ```

- Search for a term in the stored content:
  ```bash
    python search.py "AI technologies"
  ```

- Generate an article within set context: 
  ```bash
    python query.py "Tell me a joke about " --s "guardrails" --n 1
    Sure, here's a lighthearted joke about guardrails in the context of software development:

    Why was the developer afraid to play cards with the guardrails?

    Because every time they tried to deal, the guardrails kept reminding them to stay within their limits! 🚧😄
  ```

## Contributing
Contributions to enhance this demo project are welcomed. Please adhere to standard coding practices and provide documentation for your contributions.

## License
[MIT License](LICENSE.md)

## Acknowledgments
- Thanks to OpenAI for fantastic embeddings.
- Appreciation to the developers of ChromaDB.

---

*This README is part of an AI Demo Project using Codeanywhere as a sandbox environment for AI projects. It aims to guide users through the setup, usage, and contribution to the project.*