# pip install openai chromadb python-dotenv bs4 argparse lxml
from dotenv import load_dotenv
import openai
from openai import OpenAI
import chromadb
import requests
import json
import os
import logging
import asyncio
import argparse
from chromadb.db.base import UniqueConstraintError  # Import the exception
from chromadb.utils import embedding_functions
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the logging level to INFO

# Load environment variables
load_dotenv()

# Set your OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI Client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=OPENAI_API_KEY,
                model_name="text-embedding-ada-002"
            )

# Initialize ChromaDB Client
# chroma_client = chromadb.Client() # in-memory db
chroma_client = chromadb.PersistentClient(path="db") # persistent db

# Check if the collection already exists, else create it
collection_name = "sitemap_collection"
collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=openai_ef)

async def fetch_sitemap(url):
    """
    Asynchronously fetch a sitemap from the given URL.
    Returns the sitemap's XML content as a string, or None if an error occurs.
    """
    try:
        response = await asyncio.to_thread(requests.get, url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching sitemap: {e}")
        return None

def parse_sitemap(sitemap_content, max_urls=None):
    """
    Parse the sitemap content and extract a limited number of URLs.

    Args:
    sitemap_content (str): XML content of the sitemap.
    max_urls (int, optional): Maximum number of URLs to extract. If None, extracts all URLs.

    Returns:
    List[str]: A list of extracted URLs, limited to 'max_urls' if specified.
    """
    import xml.etree.ElementTree as ET

    # Parse the XML content
    tree = ET.ElementTree(ET.fromstring(sitemap_content))
    root = tree.getroot()

    # Define the namespace map for parsing sitemap XML
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Extract the URLs from the sitemap
    urls = [element.text for element in root.findall('.//ns:loc', namespace)]

    # Limit the number of URLs if max_urls is specified
    if max_urls is not None:
        urls = urls[:max_urls]

    return urls

async def fetch_and_save_html(url):
    """
    Fetch the HTML content of a given URL, extract and clean text from elements 
    with class 'page-content-container', and save it to ChromaDB.
    """
    try:
        response = await asyncio.to_thread(requests.get, url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extract elements with class 'page-content-container' and get their text
        content_elements = soup.find_all(class_='definitions')
        text_content = ' '.join(element.get_text(strip=True, separator=' ') for element in content_elements)

        save_to_chromadb(url, text_content)
    except requests.RequestException as e:
        logging.error(f"Error fetching HTML content from {url}: {e}")

def save_to_chromadb(url, html_content):
    """
    Save the HTML content to ChromaDB with detailed error handling.
    """
    try:
        collection.upsert(
            documents=[html_content],
            metadatas=[{"url": url}],
            ids=[url]
        )
    except UniqueConstraintError as e:
        logging.warning(f"Duplicate entry for {url} not added to ChromaDB: {e}")
    except Exception as e:
        # Log the exception type and message
        logging.error(f"Exception while adding/updating {url} in ChromaDB: {type(e).__name__}, {e}")

        # Optionally, log a snippet of the content for further inspection
        snippet = html_content[:200]  # Adjust the length as needed
        logging.info(f"Content snippet: {snippet}")

async def main(sitemap_url):
    """
    Main function to fetch, parse the sitemap, and save HTML content to ChromaDB.
    """
    # Fetch the sitemap
    sitemap_xml = await fetch_sitemap(sitemap_url)
    if not sitemap_xml:
        logging.error("Failed to fetch sitemap.")
        return

    # Parse the sitemap to get URLs
    urls = parse_sitemap(sitemap_xml)
    if not urls:
        logging.error("No URLs found in sitemap.")
        return

    # Fetch and save HTML content of each URL
    tasks = [fetch_and_save_html(url) for url in urls]
    await asyncio.gather(*tasks)
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch Sitemap Content.')
    parser.add_argument('sitemap_url', type=str, help='Full URL of sitemap.xml file.')
    args = parser.parse_args()

    asyncio.run(main(args.sitemap_url))