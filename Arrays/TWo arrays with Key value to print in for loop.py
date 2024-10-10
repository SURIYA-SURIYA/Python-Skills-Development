def Key_Value(names,ages):
    for name,age in zip(names,ages):
        print(f"{name}:{age}")



n=int(input("Enter The Limit : "))
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(input("Enter the Names : "))
for j in range(n):
    arr2.append(int(input("Enter the Age : ")))
    
print(arr1)
print(arr2)
print("---------------------------------------------")

print(Key_Value(arr1,arr2))