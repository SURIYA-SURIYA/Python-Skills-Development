n=int(input("Enter the Limit : "))
arr = []
value1=[]
value2 = []
for i in range(n):
    arr.append(int(input("Enter The Three Digit Values : ")))
print(arr)

for j in range(n):
    value1.append(int(arr[j] / 10))
    value2.append(int(value1[j] % 10))

#value1 = arr[0] / 10
#value2 = value1 % 10
print(value2)