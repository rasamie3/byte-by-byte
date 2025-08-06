"""
the famous factorial problem (i couldn't solve this back in college)

problem 
    we want to compute the factorial of a number n that is written as -> n!

definition
    - 0! = 1
    - 1! = 1
    - n! = n x (n-1)! of course n should be n > 1

example
    - 5! = 5 x 4 x 3 x 2 x 1
"""


# college me would be proud

def factorial(n, s=""):
    s += f"{n}"
    if n == 1 or n == 0:
        print(s)
        return 1
    s += " x "
    return n * factorial(n-1, s)

print(factorial(4))