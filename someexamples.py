# prime

def isprime(n):
    return (factors(n) == [1,n])

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i==0:
            flist = flist + [i]
    return flist

print(isprime(10))
print(isprime(11))

# primes upto n

def primesupto(n):
    primelist = []
    for i in range(1,n+1):
        if isprime(i):
            primelist = primelist + [i]
    return primelist

print(primesupto(20)) # very slow for this 2000000

# first n primes

def nprimes(n):
    (count,i,plist) = (0,1,[])
    while(count<n):
        if isprime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1
    return (plist)

print(nprimes(200)) # very slow for this 2000000

# simulate for with while

