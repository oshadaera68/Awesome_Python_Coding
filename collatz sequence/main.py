# what is collatz sequence?
"""
n=5
if n is even -> n = n / 2
if n is odd -> n = 3 * n + 1

5 -> 16 -> 8 -> 4 -> 2 -> 1
16 -> 8 -> 4 -> 2 -> 1
6 -> 3 -> 10 -> 5

cache
5 -> 16 8 4 2 1
6 -> 3 10 5
"""
import time
from functools import lru_cache


# Collatz Sequence (Iterative)
def collatz_sequence_iterative(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence


# Collatz Sequence (Iterative - Length)
def collatz_length_iterative(n):
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        counter += 1
    return counter


# Collatz Sequence (Recursive - Length)
@lru_cache(maxsize=None)
def collatz_length_recursive(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz_length_recursive(n // 2)
        else:
            return 1 + collatz_length_recursive(3 * n + 1)


longest = 0
longest_i = 1

start = time.time()
for i in range(1, 10000000):
    length = collatz_length_recursive(i)
    if length > longest:
        longest = length
        longest_i = i
end = time.time()

print(end - start)

print(longest_i)
print(longest)
