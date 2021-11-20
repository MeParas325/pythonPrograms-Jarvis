f1=open("Paras.txt")

try:
    f=open("Does2.txt")

except Exception as e:
    print(e)

except EOFError as e:
    print("EOFError aa gya hai",e)

except IOError as e:
    print("IOError aa gya hai",e)

else:
    print("This will run only when except is not running")

finally:
    print("Run this anyway")
    # f.close()
    f1.close()



print("This is a important stuff")

