import socket
import threading

# MAC adresa cílového zařízení
TARGET_MAC = "AA:BB:CC:DD:EE:FF"

# Port, na kterém server naslouchá
LISTEN_PORT = 8080


def send_wol(mac_address):
    # Odstraní oddělovače
    mac_bytes = bytes.fromhex(mac_address.replace(":", "").replace("-", ""))
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Odešle magic packet na broadcast
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ("255.255.255.255", 9))  # UDP port 9 (discard/WOL)


def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)
        print("[*] Požadavek přijat, odesílám WOL...")
        send_wol(TARGET_MAC)
        client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nWOL sent!\n")
    finally:
        client_socket.close()


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", LISTEN_PORT))
    server.listen(5)
    print(f"[*] Server naslouchá na portu {LISTEN_PORT}")

    while True:
        client, addr = server.accept()
        print(f"[*] Připojení od {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    run_server()
