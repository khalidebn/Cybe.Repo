import socket
import threading


IP = input("Enter IP address to bind the server (e.g.,): ")
Port = input("Enter Port number to bind the server (e.g., 8080): ")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, int(Port)))
    server.listen(5)
    print(f"[*] Listening on {IP}:{Port}")


    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        client_socket.send(b'ACK')

if __name__ == "__main__":
    main()