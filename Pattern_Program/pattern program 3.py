# pattern program 3:


n=int(input("enter the number :"))

for i in range(n):
    for j in range(i,n):  #(n,i) ,  (n-i)
        print("*",end="  ")
    print()
