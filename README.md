# AI Demo Project Using SDE Sandbox

## Project Overview

Welcome to our AI Demo Project, showcasing the integration and application of AI technologies in Python within SDE sandbox. This project features capabilities for generating articles using OpenAI's API, and for fetching, storing, and searching web content using [Chroma DB](https://docs.trychroma.com/).

### Main Features:
- **Sitemap Fetching and Parsing**: Automates the process of fetching sitemap XML from websites and parsing it to extract URLs.
- **Content Extraction and Storage**: Retrieves and stores web page content in ChromaDB, a versatile database system.
- **AI-Powered Search**: Employs OpenAI's embedding functions for efficient and intelligent content search within ChromaDB.
- **Article Generation**: Generates articles based on user prompts and search terms, utilizing OpenAI's GPT-4 turbo model.

## Getting Started

### Prerequisites
- Access to an SDE such as Daytona.io which supports Dev Container Specification
- Python >3.10
- OpenAI API key

### Installation
There are two ways to set up the environment for this project:

1. **Using an SDE**:
   - Users of Daytona.io, Codeanywhere, Codespaces, or VS Code can auto-configure their environment with devcontainer.json, allowing for instant start.
   - Just point the SDE to the Git repository url: https://github.com/nkkko/ai-sandbox-demo
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
   - Set up an `.env` file with your `OPENAI_API_KEY` or don't and just use the default embeddings function (all-MiniLM-L6-v2).

### Usage

1. **populate.py**: 
   - Run the script with a sitemap URL to fetch, parse, and store website content. Optionally select the embeddings function to use with `--ef`.
   - Usage: `python populate.py [SITEMAP_URL] [--n [MAX_URLS]] [--ef {default|openai}]`
   - Example: `python populate.py https://www.example.com/sitemap.xml --n 100 --ef openai`

2. **search.py**:
   - Perform searches in the stored data. Optionally select the embeddings function to use with `--ef`.
   - Usage: `python search.py [SEARCH_QUERY] [--n [NUMBER_OF_RESULTS]] [--ef {default|openai}]`
   - Example: `python search.py "example search query" --n 5 --ef default`

3. **write.py**:
   - Generate articles based on a prompt and ChromaDB search terms. Optionally select the embeddings function to use with `--ef`.
   - Usage: `python write.py [PROMPT] --s [SEARCH_TERM] --n [NUMBER_OF_RESULTS] [--ef {default|openai}]`
   - Example: `python write.py "Write an article about AI" --s "artificial intelligence" --n 3 --ef openai`

The `--ef` argument allows you to specify which [embeddings function](https://docs.trychroma.com/embeddings) to use when interacting with ChromaDB. By default, `default_ef` is used (all-MiniLM-L6-v2). If you want to use OpenAI's embeddings, specify `--ef openai`.

## Structure

- `SynthSpyder.py`: Core module containing the logic for fetching, parsing, storing, and searching.
- `populate.py`: Script for populating ChromaDB with content from a sitemap.
- `search.py`: Script to search within the stored data.
- `write.py`: Script to generate articles using OpenAI and ChromaDB to fetch context.
- `db/`: Directory containing ChromaDB client and utilities.
- `.env`: Environment file for storing your OpenAI API key.
- `.devcontainer`: Configuration directory with file for setting up the development environment automatically in supported SDEs.

## Examples

- Fetch and store 10 first articles from the sitemap:
  ```bash
    python populate.py https://www.daytona.io/sitemap-definitions.xml --n 10
  ```

- Search for the first two terms that are closest to the query in the stored content:
  ```bash
    python search.py "SDE" --n 2
  ```

- Generate an article within set context of the first result from the vector DB: 
  ```bash
    python write.py "Tell me a joke about" --s "guardrails" --n 1
  ```
  ```bash
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

*This README is part of an AI Demo Project using SDE as a sandbox environment for AI projects. It aims to guide users through the setup, usage, and contribution to the project.*