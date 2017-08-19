# not following rigid straight line sequence of execution
# getting conditional execution ability
# loops when he know condition or number of repetetions involved
#indentatio is important
#if m%n !=0:
#    (m,n) = (n,m%n)
#0 in condition is treated as false like wise "",[] is also false

# loops
y=1
z=0
for i in [1,2,3,4]:
    y=y*i
    z=z+1

print(y,z)
y=1
z=0
for i in range(1,5):
    y = y * i
    z = z + 1

print(y, z)

# factors for one number

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i==0:
            flist = flist + [i]
    return flist

print(factors(10))

# while we dont know number of repetetions but when that will reach we are not aware
