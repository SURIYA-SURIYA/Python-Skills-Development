#Normal function with addition function:
def add(a,b):
    return a+b

print(add(4,5))


# lambda :
add = lambda a,b:a+b

print(add(5,10))

twice = lambda x: x*4       #lambda using any variable can store type is 'function' 
print(type(twice))
print(twice(5))