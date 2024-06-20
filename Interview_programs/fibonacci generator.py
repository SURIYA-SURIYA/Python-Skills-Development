def fibonacci():
    a=0
    b=1

    while True:
        c = a
        a = b
        b = c+a
        yield c


        
f = fibonacci()

n = int(input("Enter your range:"))
for i in range(n):
    print(next(f),end=" ")