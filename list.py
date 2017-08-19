# creating new list from the existing one list[:]
#
factor = [0,1,2,10]
factor[0]==0
factor[0:1]==[1]

# individual access to index willreturn element whereas slicing will return, list

nested = [[2,[37]],4,["hello"]]
print(nested[0])
print(nested[0][1])
print(nested[2][0][3])
print(nested[0][1:]) # will return list of list

# list are mutable unlike string
nested[0][1] = 19
print(nested)

# mutable(same copy) vs immutable(freash copy on assignment)

x = 5
y =x
x=7
print(x,y)

list1 = [1,3,5,7]
list2 = list1
list1[2] = 7
print(list1,list2) # both list would be altered


#copying list
list3 = list1[:] # called as full slice is equal to len[0:len(l)]

#digression on equality

list1 = [1,3,5,7]
list2 = [1,3,5,7]
list3 = list2

# list1 and list2 are not equal but have equal values
# list2 and list3 are two names for same list

print(list1==list2) # true
print(list2 is list3) # true

list2[1] = 0

print(list1==list2) # false
print(list2 is list3) # true

list2 is list1

# concatenation '+', will always produce the new list

list1 = [1,3,5,7]
list2 =  list1
list1 = list1 + [9]
print(list1,list2) # lists got decapuled



