# Find second largest value in array in python

array=[2,5,7,9,4,6]

n = len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i]>array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array[-2])

#array sort method :

array=[2,5,7,9,4,6]

n = len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i]>array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array)


#array largest value Find in array :

array=[2,5,7,9,4,6]

n = len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i]>array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array[-1])


# smallest value finding in array method:

array=[2,5,7,9,4,6]

n = len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i]>array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array[0])