import time
from functools import lru_cache

@lru_cache(maxsize=int(input("How many cache you want ")))
def run(n):
    time.sleep(n)
    return n

run(3)
print("function called")
run(3)
print("function called again")
run(3)
print("function called again")
run(1)
print("function called again1")
run(2)
print("function called again1")
run(4)
print("function called again")
run(1)
print("function called again1")
run(2)
print("function called again1")
run(4)
print("function called again1")
run(5)
print("function called again2")
run(5)
print("function called again2")