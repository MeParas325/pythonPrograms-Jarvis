import time
from functools import lru_cache

@lru_cache(maxsize=32)
def work(n):
    #Some tasks taking 10 sec
    time.sleep(n)
    return n

if __name__== '__main__':
     print("Now running some work")
     work(3)
     work(1)
     work(6)
     work(9)
     work(1)
     print("Calling work 1 again")
     work(6)
     print("Calling work 6 again")
     work(9)
     print("Calling work 9 again")
     print("done....calling again")
     # input()
     work(3)
     print("Called again")

