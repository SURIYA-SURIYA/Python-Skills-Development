
#mean,median and variance



import math
max_input = int(input("Enter How many Numbers:"))
x=[]
sum=0
sum_squres=0
variance=0.0
print("Enter the Numbers:")
for i in range(0,max_input):
    x.append(int(input()))
print("The given list of number is:",x)
for i in range(0,len(x)):
    sum=sum+x[i]
mean = sum/max_input
print("Mean :",mean)
for i in range(0,max_input):
    sum_squres=sum_squres+pow(x[i]-mean,2)
variance=sum_squres/float(max_input-1)
print("Variance:",variance)
std_dev=math.sqrt(variance)
print("Standard deviation:",std_dev)