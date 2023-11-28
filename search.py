from SynthSpyder import search_in_chromadb, default_ef, openai_ef, chroma_client, collection_name
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search in ChromaDB.')
    parser.add_argument('query', type=str, help='Search query.')
    parser.add_argument('--n', type=int, default=5, help='Number of results to return.')
    parser.add_argument('--ef', type=str, default='default', choices=['default', 'openai'], help='Embedding function to use (default or openai).')
    args = parser.parse_args()

    # Select the embedding function based on the user input
    if args.ef == "openai":
        embedding_function = openai_ef
    else:
        embedding_function = default_ef

    # Initialize the collection with the selected embedding function
    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )

    # Perform the search
    results = search_in_chromadb(args.query, args.n, collection)

# Print the results
for i in range(len(results['documents'])):  # Iterate over each set of documents (outer list)
    for j in range(len(results['documents'][i])):  # Iterate over documents in each set (inner list)
        print(f"URL: {results['metadatas'][i][j]['url']}")
        print(f"Content: {results['documents'][i][j]}")  # Print the document
        print("-" * 50)