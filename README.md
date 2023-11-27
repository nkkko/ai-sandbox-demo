# AI Demo Project Using Codeanywhere

## Project Overview

Welcome to our AI Demo Project, designed to showcase the integration and application of AI technologies in Python using Codeanywhere as a sandbox environment. This project demonstrates the use of OpenAI's API and ChromaDB to fetch, store, and search web content effectively. 

### Main Features:
- **Sitemap Fetching and Parsing**: Automates the process of fetching sitemap XML from websites and parsing it to extract URLs.
- **Content Extraction and Storage**: Retrieves and stores web page content in ChromaDB, a versatile database system.
- **AI-Powered Search**: Employs OpenAI's embedding functions for efficient and intelligent content search within ChromaDB.

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

## Structure

- `main.py`: Main script for fetching and storing website content.
- `search.py`: Script to search within the stored data.
- `chromadb/`: Directory containing ChromaDB client and utilities.
- `.env`: Environment file for storing your OpenAI API key.

## Examples

- Fetch and store content:
  ```
  python main.py https://example.com/sitemap.xml
  ```

- Search for a term in the stored content:
  ```
  python search.py "AI technologies"
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