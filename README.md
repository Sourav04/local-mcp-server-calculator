# MCP Calculator Server

This project is a simple MCP server using [fastmcp](https://github.com/jlowin/fastmcp) that provides basic calculation tools: add, subtract, multiply, and divide.

## Setup

1. **Install dependencies**

   Ensure you have Python 3.10+ installed.

   and Install fasmcp using uv or pip

2. **Run the server**

   ```sh
   python server.py
   ```

   The server will start at `http://127.0.0.1:8000/mcp` (if using HTTP transport).

## Tools

- `add(a: float, b: float) -> float`
- `subtract(a: float, b: float) -> float`
- `multiply(a: float, b: float) -> float`
- `divide(a: float, b: float) -> float` (raises error if `b == 0`)

You can connect to this server using a fastmcp client or extend it with more tools as needed.

---

## Using the Test Client (via stdio)

A sample client is provided in `test_client.py` to demonstrate how to interact with the MCP server using stdio transport.

### How to Run the Client

1. Make sure you are in the `mcp` directory:
   ```sh
   cd mcp
   ```
2. Run the client:
   ```sh
   python3 test_client.py
   ```

The client will automatically start the server and print the results of the calculator tools:

```
add(5, 3) = 8.0
subtract(10, 4) = 6.0
multiply(6, 7) = 42.0
divide(20, 5) = 4.0
```

You do **not** need to start the server separately when using stdio transport with the client. 

Snapshot
<img width="1439" height="627" alt="Screenshot 2025-07-26 at 12 36 40 PM" src="https://github.com/user-attachments/assets/81329c45-3fbe-4cbc-96fc-11b6081c24db" />

