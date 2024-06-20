import datetime 
t1=datetime.datetime.now()

print(t1)
t2=t1.strftime("%Y-%M-%d %H:%M:%S")
print(t2)

currenttime= t1.time()
print("current system time",currenttime)

