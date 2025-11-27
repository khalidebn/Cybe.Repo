import socket

target_host = input("Enter target host (e.g., www.google.com): ")
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port)) 

client.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n".encode())

response = client.recv(4096)

print(response.decode())
client.close() 