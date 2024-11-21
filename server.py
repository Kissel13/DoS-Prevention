import socket
import threading
import time

# Rate limiting parameters
LIMIT = 5
WINDOW_SIZE = 10

request_counts = {}
window_start_times = {}
lock = threading.Lock()

def handle_client_message(data, client_address, server_socket):
    client_ip = client_address[0]
    now = time.time()

    with lock:
        # Get or initialize the window start time for this client
        window_start = window_start_times.get(client_ip, now)
        if now - window_start >= WINDOW_SIZE:
            # Reset the window start time and request count
            window_start_times[client_ip] = now
            request_counts[client_ip] = 1
            allowed = True
        else:
            # Within the current window
            request_count = request_counts.get(client_ip, 0)
            if request_count < LIMIT:
                request_counts[client_ip] = request_count + 1
                allowed = True
            else:
                allowed = False

    if allowed:
        response = b"Request processed.\n"
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Allowed request from {client_ip}")
    else:
        response = b"Rate limit exceeded. Try again later.\n"
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Denied request from {client_ip}")

    # Send response back to client
    server_socket.sendto(response, client_address)

def main():
    server_ip = '0.0.0.0'
    server_port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print(f"UDP Rate Limiting Server listening on {server_ip}:{server_port}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(4096)
            threading.Thread(
                target=handle_client_message,
                args=(data, client_address, server_socket)
            ).start()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
