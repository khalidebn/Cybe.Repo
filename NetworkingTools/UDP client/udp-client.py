import socket


target_host = input("Enter target host (IP or domain): ")
target_port = int(input("Enter target port (1-65535): "))

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"Hello, UDP Server!", (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()