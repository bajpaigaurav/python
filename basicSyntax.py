# assume interegs are read as binary sequence
# floats are broken down into exponents and mantissa
# division always produces float
# Qoutient operator = //
# remainder operator = %
# exponentiation operator = **
# for advanced functions log() sqrt() etc
# not loaded by default
# from math import *
# names values and types
# names dont have any inheritent type
# names type are not constant
# type(e)--> returns type of the name here 'e' is holding some value

i = 3;
j= i*2;
print(type(i))
type(j)
def divides(m,n):
    if(m%n==0):
        return True
    else:
        return False

def isEven(a):
    return(divides(a,2))
def isOdd(a):
    return(not divides(a,2))

print(isEven(10))
