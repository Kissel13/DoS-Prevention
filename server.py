# server.py

import socket
import threading

from rate_limiter import RateLimiter

class RateLimitingServer:
    def __init__(self, host='0.0.0.0', port=9999, limit='5 per 10 seconds'):
        self.host = host
        self.port = port
        # Initialize the RateLimiter with the specified limit
        self.rate_limiter = RateLimiter(limit)

    def handle_client(self, client_socket, client_address):
        client_ip = client_address[0]

        if self.rate_limiter.is_allowed(client_ip):
            # Process the request
            client_socket.send(b"Request processed.\n")
        else:
            # Deny the request
            client_socket.send(b"Rate limit exceeded. Try again later.\n")

        client_socket.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)

        print(f"Fixed Window Rate Limiting Server listening on {self.host}:{self.port}")

        try:
            while True:
                client_sock, client_address = server.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_sock, client_address)
                )
                client_thread.start()
        except KeyboardInterrupt:
            print("\nServer shutting down.")
        finally:
            server.close()