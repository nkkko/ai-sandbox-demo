import chromadb
import asyncio
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Initialize ChromaDB Client
# Replace with your path or configuration
chroma_client = chromadb.PersistentClient(path="db")

async def get_all_embeddings(collection_name):
    """
    Asynchronously retrieve all embeddings from a given collection in ChromaDB.
    """
    try:
        # Get the collection
        collection = chroma_client.get_collection(name=collection_name)

        # Query the collection to get all embeddings
        # Instead of using query_embeddings, we'll use a different approach
        results = collection.get(
            include=["embeddings"]  # Specify that we want to include embeddings in the result
        )

        return results

    except Exception as e:
        logging.error(f"Error retrieving embeddings: {e}")
        return None

# Example Usage
async def main():
    collection_name = "wikipedia_collection"  # Replace with your collection name
    embeddings = await get_all_embeddings(collection_name)
    if embeddings:
        for embedding in embeddings:
            print(embedding)
    else:
        logging.warning("No embeddings found or an error occurred.")

if __name__ == "__main__":
    asyncio.run(main())