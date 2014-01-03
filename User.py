import random
import time
class User:
    def __init__(self):
        self.identifier = str(random.randrange(2**64))
        self.timestamp = time.time()