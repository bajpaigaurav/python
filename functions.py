# starts with def
# def f(a,b,c):
#     abc
#     zya
#immutable and mutable rules apply here
# side effect can happen
# variables would have local scope inside function

# recursion

def factorial(n):
    if n <= 0:
        return(1) # base case
    else:
        val = n* factorial(n-1)
        return(val)

print(factorial(10))
