import asyncio
import os
from citekit import CiteKitClient
from citekit.mapper.gemini import GeminiMapper

mapper = GeminiMapper(model="gemini-2.5-flash", api_key=os.environ.get("GEMINI_API_KEY"))
client = CiteKitClient(mapper=mapper)

async def ingest_all():
    docs_dir = "docs"
    files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]
    
    print(f"Found {len(files)} files to ingest...\n")

    for i, filename in enumerate(files, 1):
        filepath = os.path.join(docs_dir, filename)
        resource_id = filename.replace(".md", "")
        
        print(f"[{i}/{len(files)}] Ingesting: {resource_id}")
        
        try:
            resource_map = await client.ingest(
                resource_path=filepath,
                resource_type="text",
                resource_id=resource_id
            )
            print(f"  ✓ {len(resource_map.nodes)} nodes found\n")
        except Exception as e:
            print(f"  ✗ Failed: {e}\n")

if __name__ == "__main__":
    asyncio.run(ingest_all())