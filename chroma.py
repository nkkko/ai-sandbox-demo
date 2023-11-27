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

        # Retrieve all items from the collection
        results = collection.get(
            include=["ids", "embeddings", "metadatas", "documents", "uris"]  # Include all relevant data
        )

        return results

    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return None

# Example Usage
async def main():
    collection_name = "wikipedia_collection"  # Replace with your collection name
    data = await get_all_embeddings(collection_name)
    if data:
        for item in data:
            print(f"ID: {item.get('ids')}")
            print(f"Embedding: {item.get('embeddings')}")
            print(f"Metadata: {item.get('metadatas')}")
            print(f"Document: {item.get('documents')}")
            print(f"URI: {item.get('uris')}\n")
    else:
        logging.warning("No data found or an error occurred.")

if __name__ == "__main__":
    asyncio.run(main())
