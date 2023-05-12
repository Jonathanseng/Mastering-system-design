# Python code for implementing rate limiting using the token bucket algorithm:
import time

class RateLimiter:
    def __init__(self, max_requests, per_second):
        self.max_requests = max_requests
        self.per_second = per_second
        self.tokens = max_requests
        self.last_refill_time = time.time()

    def refill_tokens(self):
        now = time.time()
        time_since_last_refill = now - self.last_refill_time
        tokens_to_add = int(time_since_last_refill * self.per_second)
        self.tokens = min(self.max_requests, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def consume(self):
        if self.tokens <= 0:
            time_to_wait = (1.0 / self.per_second) * abs(self.tokens)
            time.sleep(time_to_wait)
            self.refill_tokens()
        self.tokens -= 1

# This code defines a RateLimiter class that takes a maximum number of requests per second (max_requests) and the number of requests per second (per_second) as input parameters. The class maintains a token bucket that refills at a rate of per_second tokens per second, up to a maximum of max_requests tokens.

#The consume method of the class is used to consume a token from the bucket. If there are no tokens available, the method waits until a token becomes available. The method also calls the refill_tokens method to refill the bucket with new tokens based on the elapsed time since the last refill.

#This code can be used to limit the rate of requests to an API or service by calling the consume method before each request is made. If the rate limit is exceeded, the method will wait until a token becomes available before proceeding.




        
