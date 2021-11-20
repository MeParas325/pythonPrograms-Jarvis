def searcher():
    import time
    # Some 4 seconds time consuming task
    book="Discovery of India written by Paras"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your Name is in book")
        else:
            print("Name is not in the book")

search=searcher()
print("Search started")
next(search)
print("Next method run")
search.send("Paras")
search.close()