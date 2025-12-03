import argparse
import socket
import subprocess
import threading
import sys

# -------------------------
# CHAT MODE HANDLER
# -------------------------
def handle_chat_mode(client_socket):
    print("[*] Chat session started. Type messages and press ENTER.")

    def receive():
        while True:
            try:
                data = client_socket.recv(4096)
                if not data:
                    break
                print("\n[Remote] " + data.decode(), end="\n> ")
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        msg = input("> ")
        if msg.lower() == "exit":
            break
        client_socket.send(msg.encode())

    client_socket.close()


# -------------------------
# INTERACTIVE SHELL HANDLER
# -------------------------
def handle_shell_mode(client_socket):
    print("[*] Shell session started.")

    def receive():
        while True:
            try:
                data = client_socket.recv(4096)
                if not data:
                    break
                print(data.decode(), end="")
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        try:
            cmd = input("")
            if cmd.strip() == "":
                continue
            if cmd.lower() == "exit":
                break
            client_socket.send((cmd + "\n").encode())
        except EOFError:
            break

    client_socket.close()


# -------------------------
# SERVER LOGIC
# -------------------------
def server(args):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((args.host, args.port))
    server_socket.listen(1)

    print(f"[*] Listening on {args.host}:{args.port}...")

    client, addr = server_socket.accept()
    print(f"[*] Connection from {addr}")

    if args.shell:
        # start a real interactive shell
        proc = subprocess.Popen(
            ["/bin/bash"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        def read_output():
            for line in proc.stdout:
                client.send(line.encode())
            for line in proc.stderr:
                client.send(line.encode())

        threading.Thread(target=read_output, daemon=True).start()

        while True:
            data = client.recv(4096)
            if not data:
                break
            proc.stdin.write(data.decode())
            proc.stdin.flush()

    else:
        # CHAT MODE
        while True:
            data = client.recv(4096)
            if not data:
                break
            print("[Remote]", data.decode())
            reply = input("> ")
            client.send(reply.encode())


# -------------------------
# CLIENT LOGIC
# -------------------------
def client(args):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((args.host, args.port))

    if args.shell:
        handle_shell_mode(client_socket)
    else:
        handle_chat_mode(client_socket)


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port", type=int)
    parser.add_argument("--listen", "-l", action="store_true")
    parser.add_argument("--shell", action="store_true")  # enable remote shell
    parser.add_argument("--chat", action="store_true")   # enable chat mode

    args = parser.parse_args()

    if args.listen:
        server(args)
    else:
        client(args)
