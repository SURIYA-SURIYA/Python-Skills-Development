#comman letters find in array:

def comman_letters():
    str1 = input("enter the string of one :")
    str2 = input("enter the string of Two :")
    s1 = set(str1)
    s2 = set(str2)
    list= s1 & s2
    print(list)

comman_letters()