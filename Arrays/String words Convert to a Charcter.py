def String_Convert_Char(String):
    empty=[]
    if str == '':
        print("Please Re Enter the String")
        exit()
    else:
        for j in String:
            empty.append(j)
    return empty

try:
    str=input("Enter the Strying : ")
except TypeError:
    print("Enter String values Only")
    exit()
print(String_Convert_Char(str))
    