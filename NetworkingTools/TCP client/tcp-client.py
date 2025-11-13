import socket

target_host = input("Enter target host (IP or domain): ")
target_port = int(input("Enter target port (1-65535): "))

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the client
client.connect((target_host, target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()