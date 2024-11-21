# udp_client.py

import socket
import time

def main():
    server_ip = '10.0.0.2'
    server_port = 9999
    total_requests = 10
    delay_between_requests = 1

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(total_requests):
        try:
            client_socket.sendto(b'Hello, server!', (server_ip, server_port))
            response, _ = client_socket.recvfrom(4096)
            print(f"Request {i + 1}: {response.decode().strip()}")
        except Exception as e:
            print(f"Communication failed: {e}")
        time.sleep(delay_between_requests)

    client_socket.close()

if __name__ == '__main__':
    main()