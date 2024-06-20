print("To Find All Divisors Of An Integer :")

num = int(input("Enter The Integer :"));
for i in range(1,num+1):
    if num%i==0:
        print(i,end="")