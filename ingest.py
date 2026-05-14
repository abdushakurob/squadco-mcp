import asyncio
import os
from citekit import CiteKitClient
from citekit.mapper.gemini import GeminiMapper

mapper = GeminiMapper(model="gemini-2.0-flash", api_key=os.environ.get("GEMINI_API_KEY"))

# Use base_dir="." to ensure all generated resource maps use portable relative paths.
# Maps are stored inside the package structure for distribution.
client = CiteKitClient(
    mapper=mapper,
    base_dir=".",
    storage_dir="src/squadco_mcp/.resource_maps"
)

async def ingest_all():
    docs_dir = "src/squadco_mcp/docs"
    
    if not os.path.exists(docs_dir):
        print(f"Error: Documentation directory not found at {docs_dir}")
        return

    files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]
    print(f"Found {len(files)} files in {docs_dir} to ingest...\n")

    for i, filename in enumerate(files, 1):
        # Generate resource_id from filename (e.g., payments.md -> payments)
        filepath = os.path.join(docs_dir, filename)
        resource_id = filename.replace(".md", "")
        
        print(f"[{i}/{len(files)}] Ingesting: {resource_id}")
        
        try:
            # Ingestion uses relative paths to maintain cross-machine compatibility
            resource_map = await client.ingest(
                resource_path=filepath,
                resource_type="text",
                resource_id=resource_id
            )
            print(f"  ✓ {len(resource_map.nodes)} nodes found\n")
        except Exception as e:
            print(f"  ✗ Failed: {e}\n")

if __name__ == "__main__":
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is not set.")
    else:
        asyncio.run(ingest_all())