def Get_missing_Number_summation(a):
    n = a[-1]
    sum1 = 0
    total=n*(n+1)//2
    sum1=sum(a)
    x = total-sum1
    print("get missing number in array:",x)


a = [1,2,3,5,6,7]
Get_missing_Number_summation(a)
