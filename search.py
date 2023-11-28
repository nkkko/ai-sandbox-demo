from SynthSpider import search_in_chromadb
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search in ChromaDB.')
    parser.add_argument('query', type=str, help='Search query.')
    parser.add_argument('--n', type=int, default=5, help='Number of results to return.')
    args = parser.parse_args()

    # Perform the search
    results = search_in_chromadb(args.query, args.n)

# Print the results
for i in range(len(results['documents'])):  # Iterate over each set of documents (outer list)
    for j in range(len(results['documents'][i])):  # Iterate over documents in each set (inner list)
        print(f"URL: {results['metadatas'][i][j]['url']}")
        print(f"Content: {results['documents'][i][j]}")  # Print the document
        print("-" * 50)