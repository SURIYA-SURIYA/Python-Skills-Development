fp = open("c:\\python\\library.txt")
data=fp.read()  


lines = data.split("\n")
for line in lines:
    words = line.split(" ")
    print(words)