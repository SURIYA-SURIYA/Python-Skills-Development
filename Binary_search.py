print("Find the binary search in the program")

print("-------------------------------------")

array = []
n=int(input("Enter the Array limit : "))
for i in range(1,n+1):
    #inputvalue=int(input())
    array.append(int(input()))
print(" The array is : ",array)


E = int(input("enter search the element  : "))


M = 0
for j in array:
    if(j == E):
        print(M)
        break
    else:
        M=M+1   
       
print(M)
  