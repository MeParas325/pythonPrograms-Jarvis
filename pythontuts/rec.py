def factorial_iterative(n):
    """
    :param n: Integer
    :return: n*n-1*n-2*n-3....1
    """
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac


def factorial_recursive(n):
    """
    :param n: Integer
    :return: n*n-1*n-2*n-3....1
    """
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)

    # 5*factorial_recursive(4)
    # 5*4*factorial_recursive(4)
    # 5*4*3*factorial_recursive(4)
    # 5*4*3*2*factorial_recursive(4)
    # 5*4*3*2*1=120

#0 1 1 2 3 5 8 13
def fibo_seq(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo_seq(n-1) + fibo_seq(n-2)

number=int(input("enter the number\n"))
# print("Factorial using iterative method",factorial_iterative(number))
# print("Factorial using Recursive method",factorial_recursive(number))
print("Fibonacci sequence",fibo_seq(number))








