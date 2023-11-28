import argparse
import chromadb
from chromadb.utils import embedding_functions
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI Client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

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

def generate_article(prompt):
    """
    Generate an article using the OpenAI API.
    """
    response = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages=[
            {"role": "system", "content": "Follow user instructions. Write using Markdown."},
            {"role": "user", "content": prompt}
        ]
    )
    # Access the 'content' attribute of the last message in the response
    last_message_content = response.choices[0].message.content
    return last_message_content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an article using OpenAI and ChromaDB.')
    parser.add_argument('prompt', type=str, help='Article prompt.')
    parser.add_argument('--s', type=str, required=True, help='Search term for ChromaDB.')
    parser.add_argument('--n', type=int, default=3, help='Number of ChromaDB search results.')

    args = parser.parse_args()

    # Search in ChromaDB
    search_results = search_in_chromadb(args.s, args.n)

# Process and append search results to the prompt
additional_context = ""
for i in range(len(search_results['documents'])):  # Iterate over each set of documents (outer list)
    for j in range(len(search_results['documents'][i])):  # Iterate over documents in each set (inner list)
        additional_context += f"{search_results['documents'][i][j]}\n\n"

combined_prompt = args.prompt + "\n\n" + additional_context

# Generate the article
article = generate_article(combined_prompt)
print(article)


