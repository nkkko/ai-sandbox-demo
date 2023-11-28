# AI Demo Project Using SDE Sandbox

## Project Overview

Welcome to our AI Demo Project, showcasing the integration and application of AI technologies in Python within SDE sandbox. This project now includes features for generating articles using OpenAI's API, along with existing functionality for fetching, storing, and searching web content using ChromaDB.

### Main Features:
- **Sitemap Fetching and Parsing**: Automates the process of fetching sitemap XML from websites and parsing it to extract URLs.
- **Content Extraction and Storage**: Retrieves and stores web page content in ChromaDB, a versatile database system.
- **AI-Powered Search**: Employs OpenAI's embedding functions for efficient and intelligent content search within ChromaDB.
- **Article Generation**: Generates articles based on user prompts and search terms, utilizing OpenAI's GPT-4 model.

## Getting Started

### Prerequisites
- Access to an SDE such as Daytona.io which supports Dev Container Specification
- Python 3.x
- OpenAI API key

### Installation
There are two ways to set up the environment for this project:

1. **Using an SDE**:
   - Users of Daytona.io, Codeanywhere, Codespaces, or VS Code can auto-configure their environment with devcontainer.json, allowing for instant start.
   - Just point the SDE to the Git repository url: https://github.com/nkkko/ca-ai-demo
   - Set up an `.env` file with your `OPENAI_API_KEY`.

2. **Manual Setup**:
   - Clone the repository to your workspace or local environment.
   - Install necessary packages:
     ```
     pip install -r requirements.txt
     ```
     Or run:
     ```
     pip install openai chromadb python-dotenv bs4 argparse lxml
     ```
   - Set up an `.env` file with your `OPENAI_API_KEY`.

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
- `.devcontainer`: Configuration directory with file for setting up the development environment automatically in supported SDEs.

## Examples

- Fetch and store content:
  ```bash
    python main.py https://www.daytona.io/sitemap-definitions.xml
  ```

- Search for a term in the stored content:
  ```bash
    python search.py "SDE"
  ```

- Generate an article within set context: 
  ```bash
    python query.py "Tell me a joke about " --s "guardrails" --n 1
  ```
  ```bash
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