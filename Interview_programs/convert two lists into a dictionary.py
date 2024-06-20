#Convert two lists into a dictionary :

def list_to_dict():
    keys = [1,2,3]
    values=['apple','mango','orange']

    result = dict(zip(keys,values))

    print(result)

list_to_dict()

# Tuple to convert dictonary :

def tuple_to_dict():
    keys = (1,2,3)
    values=('apple','mango','orange')

    result =dict(zip(keys,values))

    print(result)

tuple_to_dict()

#  dict to tuple:

def dict_to_tuple():
    x = {1 :'blue',2:'red',3:'green',4:'yellow'}

    for i in x.items():
        print(i ,end="")

dict_to_tuple()