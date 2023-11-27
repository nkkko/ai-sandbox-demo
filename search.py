import argparse
import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI Embedding Function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=OPENAI_API_KEY,
                model_name="text-embedding-ada-002"
            )

# Initialize ChromaDB Client
chroma_client = chromadb.PersistentClient(path="db")

# Define the collection name
collection_name = "sitemap_collection"

# Get the collection
collection = chroma_client.get_collection(name=collection_name, embedding_function=openai_ef)

def search_in_chromadb(query, n_results):
    """
    Search in ChromaDB for the given query.

    Args:
    query (str): The search query.
    n_results (int): Number of search results to return.

    Returns:
    List of search results.
    """

    # Search in the collection
    search_results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return search_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search in ChromaDB.')
    parser.add_argument('query', type=str, help='Search query.')
    parser.add_argument('--n', type=int, default=5, help='Number of results to return')
    args = parser.parse_args()

    # Perform the search
    results = search_in_chromadb(args.query, args.n)

# Print the results
for i in range(len(results['documents'])):  # Iterate over each set of documents (outer list)
    for j in range(len(results['documents'][i])):  # Iterate over documents in each set (inner list)
        print(f"URL: {results['metadatas'][i][j]['url']}")
        print(f"Content: {results['documents'][i][j]}")  # Print the document
        print("-" * 50)

