# Lambda fumctionns or anonymous functions
# 1. Lambda function have no name
# 2. It can take any number of arguments
# 3. Lambda function can return only one value in the form of expression
# 4. It does not contain return argument
# 5. Lambda function is a one line function

# def minus(a,b):
#     return a-b

minus=lambda x,y:x-y
print(minus(9,4))

sum = lambda x, y : x + y
print(sum(4, 6))