# SquadCo API Docs MCP Server

> **Disclaimer**: This is a community-driven project and is **not affiliated with or endorsed by SquadCo**. It is built by developers, for developers, using the official public SquadCo documentation.

The SquadCo MCP Server provides your AI coding assistant (Claude, Cursor, Windsurf, etc.) with direct, structured access to the full SquadCo API documentation. 

Stop switching between your editor and the browser. Get precise API specs, validation logic, and code samples for SquadCo integrations directly in your chat.

---

## Key Features

- **Direct Knowledge**: Instant access to documentation for Payments, Transfers, Virtual Accounts, VAS, and Webhooks.
- **Accurate Specs**: Returns the exact technical markdown sections—no fuzzy hallucinations.
- **Developer Ready**: Full details on Sandbox environments, test cards, and security validation.
- **No Clone Needed**: Run directly using `uvx` or `pipx`.

---

## Capabilities

The MCP server covers the entire SquadCo ecosystem:

### 1. Payments and Collections
*   **Checkout Options**: Integration guides for the Squad Payment Modal (Inline), Redirect flows, and mobile-ready implementations.
*   **Direct API**: Technical specs for server-to-server payment initiation and transaction verification.
*   **Alternative Methods**: Documentation for POS Payment, Direct Debit, and E-commerce plugins (WooCommerce).
*   **Testing**: A comprehensive list of test card numbers, expiry dates, and CVVs for sandbox testing.

### 2. Transfers and Payouts
*   **Fund Transfers**: How to move funds from your Squad Wallet to any bank account in Nigeria.
*   **Account Lookup**: recipient name verification logic to ensure transaction accuracy.
*   **Wallet Management**: Checking ledger balances and transaction history.
*   **Bank Codes**: A complete, searchable list of all supported bank and microfinance codes.

### 3. Virtual Accounts
*   **Account Generation**: Creating dedicated virtual accounts for customers to receive automated bank transfers.
*   **Dynamic V2**: Advanced specifications for high-frequency, dynamic account creation and management.
*   **Metadata**: Attaching custom data to accounts for easier reconciliation.

### 4. Value Added Services (VAS)
*   **Airtime and Data**: API specs for selling mobile airtime and data bundles.
*   **Bills Payment**: Integration for electricity bills and other utility services.
*   **SMS Services**: Managing SMS buckets and automated messaging.

### 5. Operations and Security
*   **Webhooks**: Step-by-step setup for POST notifications, IP filtering, and signature verification.
*   **Security**: Technical guides for HMAC-SHA512 validation and AES-256 encryption/decryption.
*   **Management**: Detailed flows for Refunds, Disputes, and Chargebacks.

### 6. Sandbox and Testing
*   **Environment Setup**: Detailed information on using the `sandbox-api.squadco.com` endpoints.
*   **Test Assets**: A full database of test card numbers, CVVs, and standard OTP codes for simulating successful and failed payments.
*   **Transfer Simulation**: Specific API flows for simulating incoming bank transfers to virtual accounts in a test environment.

---

## Tools

| Tool | Purpose |
|---|---|
| `search_docs` | The main entry point. Search for any SquadCo feature (e.g., "AES encryption"). |
| `list_docs` | Browse all available API documentation files. |
| `get_doc_structure` | View the structural map of a specific document to find precise sections. |
| `resolve_section` | Fetch the full technical content, URLs, and code samples for a section. |

---

## Client Configuration Guide

### 1. Prerequisites
Before configuring your client, ensure you have the following installed on your host machine:

- **Python 3.10+**: Required to run the server logic.
- **Package Manager**: Either **uv** (recommended for speed) or **pipx**.
  - To install `uv` on Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
  - To install `uv` on macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 2. Quick Setup (Recommended)
Add one of the following to your MCP settings in Claude, Cursor, or Windsurf.

**Using uvx (Fastest):**
```json
{
  "mcpServers": {
    "squadco-docs": {
      "command": "uvx",
      "args": ["squadco-mcp"]
    }
  }
}
```

**Using pipx:**
```json
{
  "mcpServers": {
    "squadco-docs": {
      "command": "pipx",
      "args": ["run", "squadco-mcp"]
    }
  }
}
```

### 3. Client-Specific Instructions

#### Claude Desktop
1. Open the configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the `squadco-docs` entry provided above.
3. Restart Claude Desktop completely.

#### Cursor
1. Open Cursor Settings > Features > MCP Servers.
2. Click **+ Add New MCP Server**.
3. Name: `squadco-docs`
4. Type: `command`
5. Command: `uvx squadco-mcp` (If not found, use the absolute path to `uvx`).

#### Windsurf (by Codeium)
1. Add the configuration to your `mcpServers` object in `settings.json`.
2. Windows Location: `%APPDATA%\Windsurf\User\settings.json`

---

## MCP Configuration Reference

| Client | MCP Integration Method | squadco-mcp Configuration |
|---|---|---|
| Claude Desktop | JSON-RPC over stdio | Add to `mcpServers` in `claude_desktop_config.json` |
| Cursor | Native MCP UI | Use `uvx squadco-mcp` as the command |
| Windsurf | Cascade MCP | Add to `mcpServers` in `settings.json` |
| VS Code | Workspace MCP | Add to `.vscode/mcp.json` |
| Claude Code | CLI MCP Manager | Run `claude mcp add squadco-mcp -- uvx squadco-mcp` |

---

## Troubleshooting Tips

- **Command Not Found**: If your client says `uvx` or `pipx` is not found, it is likely because the installation directory is not in your system's PATH. 
  - **Windows Fix**: Restart your PC or use the absolute path to the executable (e.g., `C:\Users\YourName\.local\bin\uvx.exe`).
- **Restart Required**: Most desktop clients (Claude, Cursor) require a full restart (not just closing the window) to pick up changes made to JSON configuration files or the system PATH.
- **Python Version**: Ensure you are using Python 3.10 or higher. You can check this by running `python --version` in your terminal.
- **Connection Errors**: If the server fails to connect, check the developer console in your client (usually Ctrl+Shift+I) for specific JSON-RPC errors.

---

## Technical Details

The SquadCo MCP Server uses [CiteKit](https://abdushakurob.github.io/citekit) (by [@abdushakurob](https://github.com/abdushakurob)) to provide high-fidelity documentation access to AI agents.

Unlike standard RAG (Retrieval-Augmented Generation) which uses vector-based similarity, this server employs a structural mapping approach:

- **Pre-computed Mapping**: Documentation is analyzed during ingestion to create a structural index of all API endpoints, parameters, and code blocks.
- **Deterministic Resolution**: The AI assistant identifies the specific node it needs from the map and resolves the content locally from the bundled markdown files.
- **Precision Context**: By resolving exact sections rather than chunked text, the server ensures the AI receives clean, relevant context without noise.

**Stack:**
- **Core Engine**: [CiteKit](https://abdushakurob.github.io/citekit)
- **Scraper**: [crawl4ai](https://github.com/unclecode/crawl4ai)
- **Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---