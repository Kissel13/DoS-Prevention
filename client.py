# client.py

import socket
import time

def main():
    server_ip = 'localhost'  # Change this to the server's IP if running remotely
    server_port = 9999
    total_requests = 10      # Total number of requests to send
    delay_between_requests = 1  # Delay in seconds between requests

    for i in range(total_requests):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((server_ip, server_port))
            # Send data to the server
            client.send(b'Hello, server!')
            response = client.recv(4096)
            print(f"Request {i + 1}: {response.decode().strip()}")
        except Exception as e:
            print(f"Connection failed: {e}")
        finally:
            client.close()
        time.sleep(delay_between_requests)

if __name__ == '__main__':
    main()