import time

class RateLimiter:
    def __init__(self, limit=1, window=10):
        """
        Initializes the rate limiter.
        :param limit: Maximum requests allowed in the time window.
        :param window: Time window in seconds.
        """
        self.limit = limit
        self.window = window
        self.request_log = {}  # Dictionary to track requests per IP
        self.blacklist = {}  # Set to track permanently blacklisted IPs

    def is_allowed(self, user_identifier):
        """
        Checks if a request is allowed based on rate limiting and blacklisting.
        :param user_identifier: Unique identifier for the user (e.g., IP address).
        :return: True if allowed, False otherwise.
        """
        current_time = time.time()

        # Debugging: Print the current time
        print("Current time: " + str(current_time))

        # Check if the user is blacklisted
        if user_identifier in self.blacklist:
            print("User " + user_identifier + " is blacklisted.")
            return False  # Deny the request

        # Initialize request log for new users
        if user_identifier not in self.request_log:
            self.request_log[user_identifier] = []
            print("New user " + user_identifier + " initialized.")

        # Remove expired entries from the request log
        self.request_log[user_identifier] = [
            t for t in self.request_log[user_identifier] if current_time - t < self.window
        ]

        # Debugging: Print the request log for the user
        print("Request log for " + user_identifier + ": " + str(self.request_log[user_identifier]))
	
        if len(self.request_log[user_identifier]) >= self.limit:
            print("Rate limit exceeded. Adding " + user_identifier + " to the blacklist.")
            self.blacklist[user_identifier] = current_time + 300  # Blacklist for 300 seconds
            return False

        # Enforce rate limit
        if len(self.request_log[user_identifier]) >= self.limit:
            print("User " + user_identifier + " exceeded the rate limit. Permanently blacklisting.")
            self.blacklist[user_identifier] = current_time  # Add the IP to the blacklist with a timestamp
            return False

        remaining_requests = self.limit - len(self.request_log[user_identifier])
        print("User " + user_identifier + " is " + str(remaining_requests) + " requests away from being blacklisted.")

        # Log the request
        self.request_log[user_identifier].append(current_time)
        print("Packet from " + user_identifier + " allowed.")
        return True