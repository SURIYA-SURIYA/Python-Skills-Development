#HoW to Reverse a list in python

"""
 1.reverse
 2.Slicing
 3.loop
"""
#reverse

list1 = [10,20,78,56]
list1.reverse()

print(list1)

#reversed

list2 = reversed(list1)
print(list2)

#Sliceing

list3=list1[::-1]
print(list3)

#Looping with reverse
list5 = []
list = [4,7,8,5]

for i in range(len(list)-1,-1,-1):
    list5.append(list[i])
print(list5)


