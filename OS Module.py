
# os module in Python



import os

print(os.name)
print(os.getcwd)          #get current working directorty
print(os.chdir("c://"))  #change working directory
print(os.getcwd)

print(os.makedirs('new//new2'))     #make directorys
print(os.removedirs('new/new2'))     #remove directorys

print(os.listdir())    # view list of directorys

# clear commend prompt
clear = lambda:os.system('cls')
clear() 