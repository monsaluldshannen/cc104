import time
# O(1) access
arr = list(range(1_000_000))
start = time.time()
x = arr[500_000]   # constant time
end = time.time()
print("O(1) access time:", end - start)
# O(n) search
target = 999_999
start = time.time()
found = target in arr  # linear search
end = time.time()
print("O(n) search time:", end - start)