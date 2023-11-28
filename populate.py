from SynthSpider import fetch_sitemap, parse_sitemap, fetch_and_save_html
import argparse
import asyncio
from tqdm import tqdm

async def main(sitemap_url, n):
    """
    Main function to fetch, parse the sitemap, and save HTML content to ChromaDB.
    """
    # Fetch the sitemap
    sitemap_xml = await fetch_sitemap(sitemap_url)
    if not sitemap_xml:
        logging.error("Failed to fetch sitemap.")
        return
    else:
        print(f"Successfully fetched: {sitemap_url}")

    # Parse the sitemap to get URLs
    urls = parse_sitemap(sitemap_xml, n)
    if not urls:
        logging.error("No URLs found in sitemap.")
        return

    # Set up the progress bar
    pbar = tqdm(total=len(urls))

    # Function to update the progress bar
    def update_progress():
        pbar.update(1)

    # Fetch and save HTML content of each URL
    tasks = [fetch_and_save_html(url, update_progress) for url in urls]
    await asyncio.gather(*tasks)
    
    pbar.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch Sitemap Content.')
    parser.add_argument('sitemap_url', type=str, help='Full URL of sitemap.xml file.')
    parser.add_argument('--n', type=int, default=None, help='Number of results to return.')
    args = parser.parse_args()

    asyncio.run(main(args.sitemap_url, args.n))