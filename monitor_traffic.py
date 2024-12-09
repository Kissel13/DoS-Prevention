from rateLimit import RateLimiter  # Import the RateLimiter class from rateLimiterV2

# Driver program to simulate Mininet traffic monitoring
def main():
    rate_limiter = RateLimiter(limit=1, window=10)  # Initialize the rate limiter
    print("Starting rate limiter on victim host (h1)...")

    # Simulated incoming traffic from other hosts
    while True:
        try:
            src_ip = input("Enter source IP (or type 'exit' to stop): ").strip()
            if src_ip.lower() == 'exit':  # Exit the program if 'exit' is typed
                print("Exiting rate limiter.")
                break

            # Check if the request is allowed
            if rate_limiter.is_allowed(src_ip):
                print("Packet from {} allowed.".format(src_ip))
            else:
                print("Packet from {} denied.".format(src_ip))
        except KeyboardInterrupt:  # Handle manual interruption (Ctrl+C)
            print("\nRate limiter stopped.")
            break


if __name__ == "__main__":
    main()
