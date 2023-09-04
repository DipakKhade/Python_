# Function Caching in Python | Python Tutorial - Day #92

from functools import lru_cache

import time

@lru_cache(maxsize=None)   # this will store a cache in memory
def fx(n):
    time.sleep(5)
    return n*6


print(fx(20))
print('done for 20')
print(fx(18))
print('done for 18')
print(fx(7))
print('done for 7')

# the follwing result is directly printed , since the values are already calculated above and sotred in cache
print(fx(20))
print('done for 20')
print(fx(18))
print('done for 18')
print(fx(7))
print('done for 7')

