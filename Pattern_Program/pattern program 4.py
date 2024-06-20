#pattern program 4:


n=int(input("enter the number :"))

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i*2+1):
        print("*",end=" ")
    print()
"""
output  :

          * 
        * * * 
      * * * * *
    * * * * * * *
  * * * * * * * * *

  """