# TCP Client (tcp-client.py)

Simple TCP client script that connects to a target host and port, sends a basic HTTP GET request, and prints the response.

This script is intended as a small networking utility / teaching example. It uses Python's built-in `socket` module.

## File
- tcp-client.py

## Requirements
- Python 3.x

## Description
The script:
1. Prompts the user for a target host (IP address or domain) and a target port (1-65535).
2. Creates a TCP socket and connects to the target.
3. Sends a simple HTTP GET request (`GET / HTTP/1.1`) with the provided Host header.
4. Receives up to 4096 bytes from the remote host and prints the decoded response.
5. Closes the connection.

Note: This is a very small example and does not implement timeouts, retries, or a robust receive loop. For production use or scanning, improve error handling and respect legal/ethical considerations.

## Usage
1. Clone or download the repository and navigate to the folder containing `tcp-client.py`.
2. Run the script with Python 3:

```
python3 "tcp-client.py"
```

3. When prompted, enter:
- Target host: an IP address or domain (e.g., `example.com` or `93.184.216.34`)
- Target port: an integer between 1 and 65535 (e.g., `80`)

Example session:
```
Enter target host (IP or domain): example.com
Enter target port (1-65535): 80
HTTP/1.1 200 OK
...
```

## Example
To fetch the homepage from example.com on port 80:
- Host: example.com
- Port: 80

The script will send:
```
GET / HTTP/1.1
Host: example.com
```
and print the beginning of the HTTP response.

## Limitations & Improvements
- The script reads only a single `recv(4096)` chunk. For larger responses, implement a loop to read until the connection is closed or a content-length/transfer-encoding policy is handled.
- No timeout is set — the script may hang if the server does not respond. Consider `client.settimeout(seconds)`.
- Minimal error handling: currently it will raise exceptions for DNS failures, connection refusals, or invalid input. Wrap operations in try/except blocks to handle errors gracefully.
- Does not validate input beyond casting the port to int. Add checks for port range and host format if required.

## Security & Legal Notice
Do not use this script to scan, probe, or attack systems you do not own or have explicit permission to test. Unauthorized scanning or access can be illegal and unethical.

## Contributing
Feel free to open issues or pull requests to add features like timeouts, receive loops, TLS support, or argument parsing.

## License
Include or replace with your license of choice. (No license file included in this directory by default.)

## Author
Original file by: khalidebn
