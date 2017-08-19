# List are mutable
list1 = [1,3,5,7]
list2= list1
list1[2] = 7
print(list1,list2)

# both lists got chnaged

list1 = [1,3,5,7]
list2= list1

list1 = list1[0:2] + [7] + list1[3:]

print(list1,list2) # list2 was not affected

# extending the list one way using + operator but would create new list

# other wise we can use append

list1 = [1,3,5,7]
list2 = list1
list1.append(12)

print(list1,list2)

list1.extend([2,3,4]) # takes list as argument

print(list1)

# remove an element

list1.remove(2) # gives error if the element is not present and it will rmove first occurance only

print(list1)

# slice replacement important one, exapand inplace(will not creat new list)

list1 = [1,3,4,5]
list1[2:] = [7,8]
print(list1)
list1[2:] = [9,0,8,10]

print(list1)

# shrink

list1[3:] = [1]

print(list1)

# finding value is there in list or now

# x in list1

if 1 in list1:
    list1.remove(1)

print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)

list1.index(2) ## find rightmost of x in l

# for other refer documentation







