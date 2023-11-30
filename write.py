from SynthSpider import search_in_chromadb, write_article, default_ef, openai_ef, chroma_client, collection_name
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an article using OpenAI and ChromaDB.')
    parser.add_argument('prompt', type=str, help='Article prompt.')
    parser.add_argument('--s', type=str, required=True, help='Search term for ChromaDB.')
    parser.add_argument('--n', type=int, default=5, help='Number of ChromaDB search results.')
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

    # Search in ChromaDB
    search_results = search_in_chromadb(args.s, args.n, collection)

    # Process and append search results to the prompt
    additional_context = ""
    for i in range(len(search_results['documents'])):  # Iterate over each set of documents (outer list)
        for j in range(len(search_results['documents'][i])):  # Iterate over documents in each set (inner list)
            additional_context += f"{search_results['documents'][i][j]}\n\n"

    combined_prompt = args.prompt + "\n\n" + additional_context

    # Generate the article
    article = write_article(combined_prompt)
    print(article)
