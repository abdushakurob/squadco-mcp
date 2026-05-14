import asyncio
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

async def crawl_squadco():
    print("Starting crawl of SquadCo docs...")
    os.makedirs("docs", exist_ok=True)

    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=3,
            include_external=False,
            max_pages=100,
        ),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(
            url="https://docs.squadco.com",
            config=config
        )

        print(f"\nCrawl complete! Found {len(results)} pages.")

        for i, result in enumerate(results, 1):
            if not result.success:
                print(f"[{i}] Skipped (failed): {result.url}")
                continue

            slug = (
                result.url
                .replace("https://docs.squadco.com/", "")
                .strip("/")
                .replace("/", "_")
                or "index"
            )
            filepath = f"docs/{slug}.md"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Source: {result.url}\n\n")
                f.write(result.markdown or "")

            print(f"[{i}/{len(results)}] Saved: {filepath}")

    print("\nDone. All docs saved to 'docs/' directory.")

if __name__ == "__main__":
    asyncio.run(crawl_squadco())