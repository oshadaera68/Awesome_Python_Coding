from functools import cache, lru_cache
import time


@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 2)


start = time.time()
print(fibonacci(400))
end = time.time()

print(end - start)
