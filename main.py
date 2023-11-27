from dotenv import load_dotenv
import openai
from openai import OpenAI
import chromadb
import requests
import json
import os
import logging
import asyncio

# Load environment variables
load_dotenv()

# Set your OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI Client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize ChromaDB Client
# chroma_client = chromadb.Client() # in memory db
chroma_client = chromadb.PersistentClient(path="db") # persistent db
collection = chroma_client.create_collection(name="wikipedia_collection")

# Configure Logging
logging.basicConfig(level=logging.INFO)

async def fetch_wikipedia_page(title):
    """
    Asynchronously fetch the content and title of a Wikipedia page.
    Returns title and content or title and None if content is not found.
    """
    URL = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&titles={title}&redirects=true"
    try:
        response = await asyncio.to_thread(requests.get, URL)
        response.raise_for_status()
        data = response.json()
        page = next(iter(data['query']['pages'].values()), None)

        if page and 'extract' in page:
            return title, page['extract']
        else:
            return title, None
    except requests.RequestException as e:
        logging.error(f"Error fetching Wikipedia page: {e}")
        return title, None

async def compute_embeddings(text):
    """
    Asynchronously compute embeddings for a given text using OpenAI.
    """
    try:
        response = await asyncio.to_thread(
            openai_client.embeddings.create,
            input=[text],
            model="text-embedding-ada-002"
        )

        # Correctly accessing the embedding data
        if response.data and len(response.data) > 0:
            embedding = response.data[0].embedding
            return embedding
        else:
            logging.warning("No embedding data found in response.")
            return None

    except openai.APIError as e:
        logging.error(f"Error computing embeddings: {e}")
        return None

async def add_to_chromadb(title, content):
    """
    Asynchronously add Wikipedia content and its embeddings to ChromaDB.
    """
    embedding = await compute_embeddings(content)
    if embedding:
        collection.add(
            documents=[content],
            embeddings=[embedding],
            metadatas=[{"title": title}],
            ids=[title]
        )
    else:
        logging.warning(f"Failed to add {title} to ChromaDB due to missing embeddings.")

# Example Usage
async def main():
    title, content = await fetch_wikipedia_page("Pythonidae")
    if content:
        await add_to_chromadb(title, content)
    else:
        logging.warning(f"Content not found for {title}")

if __name__ == "__main__":
    asyncio.run(main())