from SynthSpider import search_in_chromadb, write_article
import argparse

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
article = write_article(combined_prompt)
print(article)