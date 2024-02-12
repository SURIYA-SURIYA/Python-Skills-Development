#import the nessery modules
import string
import random

#input the length of passwords
length = int(input("Enter the password length:"))

#Define data

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#compine the data
all = lower + upper + num + symbols

temp = random.sample(all,length)

#create the password

password = "".join(temp)

#print the password
if (length >= 4):
    print("password :" ,password)
    
else:
    print("your password length morethan 4")


