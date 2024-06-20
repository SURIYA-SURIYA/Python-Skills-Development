print("Find the linear search in the program")

print("-------------------------------------")

array = []
n=int(input("Enter the Array limit : "))
for i in range(1,n+1):
    #inputvalue=int(input())
    array.append(int(input()))
print(" The array is : ",array)


E = int(input("enter search the element : "))

for j in array:
    if (j == E):
        print(j)
    else:
        print("The element is not the array value")
    
