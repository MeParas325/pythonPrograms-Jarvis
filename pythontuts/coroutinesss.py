def searcher():
    import time
    # Some 4 seconds time consuming task
    book="Discovery of India written by Jawahar lal nehru"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in book")
        else:
            print("Text is not in the book")

search=searcher()
print("Search started")
next(search)
print("Next method run")
search.send("of")
search.close()
# input("Press any key")
# search.send("of India")
# input("Press any key")
# search.send("lal")
# input("Press any key")
# search.send("lal nehru")
# input("Press any key")
# search.send("lal nehruu")
