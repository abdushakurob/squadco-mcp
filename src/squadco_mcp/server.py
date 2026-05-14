import os
from mcp.server.fastmcp import FastMCP
from citekit import CiteKitClient

mcp = FastMCP("squadco-docs")

# Absolute path to this package folder
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize CiteKit with absolute paths
# base_dir is the root where 'docs/' folder lives
client = CiteKitClient(
    base_dir=PACKAGE_DIR, 
    storage_dir="resource_maps"
)

@mcp.tool()
def search_docs(query: str) -> str:
    """Search across all available documentation for specific keywords or features."""
    try:
        results = client.search(query)
        if not results:
            return f"No documentation found matching: {query}"
        
        output = [f"Found {len(results)} matches for '{query}':\n"]
        for doc_id, node in results:
            output.append(f"- [{doc_id}] {node.title} (ID: {node.id})")
            if node.summary:
                output.append(f"  Summary: {node.summary}")
        
        return "\n".join(output)
    except Exception as e:
        return f"Search failed: {str(e)}"

@mcp.tool()
def list_docs() -> str:
    """List all available SquadCo API documentation modules."""
    return "Available documentation IDs:\n" + "\n".join(client.list_maps())

@mcp.tool()
def get_doc_structure(doc_id: str) -> dict:
    """Retrieve the hierarchical structure of a specific document."""
    try:
        return client.get_structure(doc_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def resolve_section(doc_id: str, section_id: str) -> str:
    """Fetch the precise technical content of a specific documentation node."""
    try:
        # v0.2.1 handles the paths and slicing natively
        evidence = client.resolve(doc_id, section_id)
        
        if evidence.output_path and os.path.exists(evidence.output_path):
            with open(evidence.output_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            return f"--- Source: {evidence.address} ---\n\n{content}"
        
        return "Error: Extraction failed or file not found."
    except Exception as e:
        return f"Resolution error: {str(e)}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
