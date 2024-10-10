def Sort_String(n,arr):
    for j in range(0,n):
        for k in range(j+1,n):
            if arr[j]>arr[k]:
                temp = arr[j]
                arr[j]=arr[k]
                arr[k]=temp
    return arr



n=int(input("Enter The Limit : "))
arr=[]
for i in range(n):
    arr.append(input("Enter the Words : "))
    
print(arr)
print(Sort_String(n,arr))