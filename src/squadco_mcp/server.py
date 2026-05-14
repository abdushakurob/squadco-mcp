import os
import json
from mcp.server.fastmcp import FastMCP
from citekit import CiteKitClient

mcp = FastMCP("squadco-docs")

# Get the absolute path to the directory where server.py is located
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize client using official base_dir and storage_dir parameters
# This ensures it finds the bundled .resource_maps relative to the package
client = CiteKitClient(base_dir=CURRENT_DIR, storage_dir=".resource_maps")

@mcp.tool()
def list_docs() -> str:
    """List all available SquadCo API documentation files."""
    try:
        maps = client.list_maps()
        return "Available documentation IDs:\n" + "\n".join(maps)
    except Exception as e:
        return f"Error listing docs: {str(e)}"

@mcp.tool()
def search_docs(query: str) -> str:
    """
    Search for documentation sections by title or summary.
    Use this when you aren't sure where a specific feature (e.g. "AES encryption") is documented.
    """
    query = query.lower()
    results = []
    
    try:
        doc_ids = client.list_maps()
        for doc_id in doc_ids:
            doc_map = client.get_map(doc_id)
            
            # Helper to recursively search nodes
            def search_nodes(nodes):
                for node in nodes:
                    title = (node.title or "").lower()
                    summary = (node.summary or "").lower()
                    
                    if query in title or query in summary:
                        results.append(
                            f"- **{doc_id}** -> `[{node.id}]` {node.title}\n"
                            f"  _{summary or 'No summary available.'}_"
                        )
                    
                    if node.children:
                        search_nodes(node.children)

            search_nodes(doc_map.nodes)
            
    except Exception as e:
        return f"Error searching docs: {str(e)}"
                
    if not results:
        return f"No documentation sections found matching '{query}'."
    
    # Return top 15 matches to keep context window clean
    return "### Search Results\n\n" + "\n\n".join(results[:15])

@mcp.tool()
def get_doc_structure(doc_id: str) -> str:
    """
    Get the structure/nodes of a specific document.
    Use this to see what sections are available before resolving.
    """
    try:
        # Get the map and return a summary of its nodes
        doc_map = client.get_map(doc_id)
        
        lines = [f"Structure for '{doc_id}':"]
        for node in doc_map.nodes:
            lines.append(f"- [{node.id}] {node.title}")
            for sub in node.children:
                lines.append(f"  - [{sub.id}] {sub.title}")
        
        return "\n".join(lines)
    except Exception as e:
        return f"Error getting structure: {str(e)}"

@mcp.tool()
def resolve_section(doc_id: str, section_id: str) -> str:
    """
    Fetch the full content of a specific documentation section.
    Provide the doc_id (e.g. 'payments') and the section_id (e.g. 'standard-test-cards').
    """
    try:
        # Using citekit to resolve the content
        evidence = client.resolve(doc_id, section_id)
        
        # Read the extracted content
        if evidence.output_path and os.path.exists(evidence.output_path):
            with open(evidence.output_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            return f"## {evidence.node.title}\n\n{content}"
        else:
            return f"Could not resolve content for {doc_id}/{section_id}"
            
    except Exception as e:
        return f"Error resolving section: {str(e)}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
