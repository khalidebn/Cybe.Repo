# TCP Server (tcp-server.py)

A minimal, single-file TCP server that accepts connections and allows the operator to read an incoming message and reply interactively.

This repository file: `NetworkingTools/TCP server/tcp-server.py`

## Features
- Listens on a user-provided IP and port.
- Accepts multiple clients using Python threads (one thread per connection).
- Prints received client data and prompts the operator to type a response to send back.

## Requirements
- Python 3.6+ (tested with 3.8+)
- No external libraries required (uses the standard library `socket` and `threading` modules)

## Usage

1. Open a terminal and run the server script:

```bash
python "NetworkingTools/TCP server/tcp-server.py"
```

2. When prompted, enter the IP address to bind to (for local testing use `127.0.0.1` or `0.0.0.0` to bind all interfaces) and a port number (e.g., `8080`):

```
Enter IP address to bind the server (e.g.,): 127.0.0.1
Enter Port number to bind the server (e.g., 8080): 8080
[*] Listening on 127.0.0.1:8080
```

3. Connect from a client. Options:

- Using netcat (Linux/macOS):

```bash
nc 127.0.0.1 8080
```

Type a message in the netcat session and press Enter. The server will print the message and prompt the operator to type a response.

- Using telnet:

```bash
telnet 127.0.0.1 8080
```

- Using a simple Python client:

```python
# sample_client.py
import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.create_connection((HOST, PORT)) as s:
    s.sendall(b"Hello from client\n")
    resp = s.recv(4096)
    print("Server replied:", resp.decode())
```

Run:

```bash
python sample_client.py
```

## Example interaction

Server terminal:

```
[*] Accepted connection from 127.0.0.1:53514
[*] Received: Hello from client
Enter a msg to send to the client: Hi client — got your message!
```

Client terminal will display the server's reply.

## Notes & Caveats
- This is a learning/example script — do not use as-is in production.
- The server uses blocking I/O per thread; a large number of simultaneous clients may exhaust system resources.
- There is no authentication or encryption (no TLS). For real deployments use TLS and proper authentication.
- The server accepts operator input for every message received; that makes automation/testing harder. Consider changing to an automated response or a protocol.

## Suggested improvements
- Fix the small typo in the server file (variable name `repsonse` -> `response`).
- Add argument parsing (e.g., `argparse`) so IP/port can be passed as CLI flags.
- Add graceful shutdown handling (catch SIGINT and close server socket).
- Add logging instead of print statements.
- Consider using non-blocking IO libraries (asyncio) or a connection pool for better scalability.
- Add size checks and input validation for received data.

A minimal corrected `handle_client` example:

```python
def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        response = input("Enter a msg to send to the client: ")
        client_socket.send(response.encode('utf-8'))
```

## Troubleshooting
- If you see "Address already in use", choose another port or kill the process using that port.
- To allow connections from other machines, bind to `0.0.0.0` and ensure firewall/host rules allow the port.
- On Windows, use `ncat`/`telnet` or the Python client to test connections.

## License
This file is provided as-is for learning and demonstration purposes. No license specified in the repository — add one if you plan to reuse or distribute it.
