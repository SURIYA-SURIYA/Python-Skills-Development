def Missing_element(n,arr):
    arr.sort()
    miss_element= []
    for i in range(n-1):
        if arr[ i+1 ] - arr[i] > 1:
            for j in range(arr[i]+1,arr[i+1]):
                miss_element.append(j)
    return miss_element

n=int(input("Enter the Limit : "))
arr=[]
for k in range(n):
    arr.append(int(input("Enter the Elements : ")))
print(arr)
print(Missing_element(n,arr))

'''
n=4
arr=[1,2,4,6]
print(Missing_element(n,arr))
'''