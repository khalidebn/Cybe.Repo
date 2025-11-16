# UDP Client (udp-client.py)

Simple UDP client script that sends a datagram to a target host and port, then waits for a single response. This script is intended as a small networking utility / teaching example and uses Python's built-in `socket` module.

## File
- udp-client.py

## Requirements
- Python 3.x

## Description
The script:
1. Prompts the user for a target host (IP address or domain) and a target port (1-65535).
2. Creates a UDP socket (socket.SOCK_DGRAM).
3. Sends a short message (`"Hello, UDP Server!"`) to the target host and port using `sendto`.
4. Receives up to 4096 bytes from the remote host using `recvfrom` and prints the decoded response.
5. Closes the socket.

## Usage
1. Clone or download the repository and navigate to the folder containing `udp-client.py`.
2. Run the script with Python 3:

python3 "udp-client.py"

3. When prompted, enter:
- Target host: an IP address or domain (e.g., `example.com` or `127.0.0.1`)
- Target port: an integer between 1 and 65535 (e.g., `12345`)

Example session:
Enter target host (IP or domain): localhost
Enter target port (1-65535): 9999
Hello from server!

## Example
To send a datagram to a UDP echo server running locally on port 9999:
- Host: localhost
- Port: 9999

The script will send the bytes `Hello, UDP Server!` and print the first received reply.

## Limitations & Improvements
- Single receive call: The script performs a single `recvfrom(4096)`. For more complex protocols or larger responses, implement a loop or protocol-aware parsing.
- No timeouts: The socket has no timeout and may block indefinitely if no response arrives. Consider using `client.settimeout(seconds)` or non-blocking sockets with `select`.
- Minimal error handling: Add try/except blocks to handle DNS failures, invalid input, connection errors, or keyboard interrupts gracefully.
- Input validation: The script converts port to int but does not validate range. Add checks for port range and host format.
- CLI support: Add `argparse` to accept host and port as command-line arguments for automation or scripting.
- Security: The script sends a fixed payload and is not encrypted. If sending sensitive data, use secure channels (e.g., DTLS or an application-layer encryption).

## Security & Legal Notice
Do not use this script to scan, probe, or attack systems you do not own or have explicit permission to test. Unauthorized scanning or access can be illegal and unethical.

## Contributing
Contributions are welcome. Suggestions:
- Add timeout and retry logic
- Support command-line arguments (argparse)
- Add logging and verbose/debug modes
- Add tests or examples for common UDP services (DNS, NTP, custom echo server)

## License
Add or replace with your preferred license. (No license file included by default.)

## Author
Original file by: khalidebn
