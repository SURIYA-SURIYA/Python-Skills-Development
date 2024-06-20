

#python prime or not


num=int(input("enter the value :"))

if num > 1:


    for i in range(2,int(num/2)+1):
        if (num%i)==0:
            print(num,"is a  not prime number")
            break
    else:
        print(num,"a prime number")

else:
    print(num,"is not a prime number")
