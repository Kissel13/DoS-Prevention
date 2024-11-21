# rate_limiter.py

from limits import parse
from limits.storage import MemoryStorage
from limits.strategies import FixedWindowRateLimiter

class RateLimiter:
    def __init__(self, limit_string='5 per 10 seconds'):
        # Parse the rate limit string (e.g., '5 per 10 seconds')
        self.rate_limit = parse(limit_string)
        # Initialize storage (in-memory for simplicity)
        self.storage = MemoryStorage()
        # Initialize the fixed window rate limiter
        self.limiter = FixedWindowRateLimiter(self.storage)

    def is_allowed(self, user_identifier):
        # Check if the request is allowed for the given user
        return self.limiter.hit(self.rate_limit, user_identifier)