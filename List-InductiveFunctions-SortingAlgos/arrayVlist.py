# fixed array, expanion and contraction are costly operation
# list flexible,plumbing is easy
# operations : exchange in array constant time ! linear in list
# binary search:
# questions is it imp whether seq be as an array or list will that affect

# basic way to search someting in python in unsorted seq
def search(seq,key):
    for v in seq :
        if v == key:
            return True
    return False

# when seq is sorted !
# compare v with midpoint of seq
# if midpoint is v=key then it found
# if v<midpoint then search in left part
# if v > mipoint search in right part

def bsearch(seq,v,l,r):

    if(r-l==0):
        return false
    mid = (l+r)//2 # integer division

    if(v == seq[mid]):
        return True
    if(v<seq[mid]):
        return (bsearch(seq,v,l,mid))
    else:
        return (bsearch(seq,v,mid+1,r))

# how long will this take ?
# list in python hybrid between list and arrays
print(bsearch([1,2,3,4,5],3,0,6))
