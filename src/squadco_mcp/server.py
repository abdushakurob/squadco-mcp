import os
import json
from mcp.server.fastmcp import FastMCP
from citekit import CiteKitClient

mcp = FastMCP("squadco-docs")

# Locate the absolute path of the package directory for reliable resource resolution
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize CiteKit with the package root as base_dir to resolve bundled maps and docs
client = CiteKitClient(base_dir=CURRENT_DIR, storage_dir=".resource_maps")

@mcp.tool()
def list_docs() -> str:
    """List all available SquadCo API documentation modules."""
    try:
        maps = client.list_maps()
        return "Available documentation IDs:\n" + "\n".join(maps)
    except Exception as e:
        return f"Error listing docs: {str(e)}"

@mcp.tool()
def search_docs(query: str) -> str:
    """
    Search documentation nodes by title or summary for specific features or endpoints.
    Returns the top 15 matches to maintain context efficiency.
    """
    query = query.lower()
    results = []
    
    try:
        doc_ids = client.list_maps()
        for doc_id in doc_ids:
            doc_map = client.get_map(doc_id)
            
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
    
    return "### Search Results\n\n" + "\n\n".join(results[:15])

@mcp.tool()
def get_doc_structure(doc_id: str) -> str:
    """Retrieve the hierarchical structure of a specific document to identify available sections."""
    try:
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
    """Fetch and return the full technical content of a specific documentation node."""
    try:
        evidence = client.resolve(doc_id, section_id)
        
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
