def reverse_words(string):
  
    # Split words in the given string
    # and reverse the order
    reversed_words = string.split()[::-1]
    
    # Join the reversed words into a 
    # single string
    return " ".join(reversed_words)

# Input string
string = " geeks for all"
print(reverse_words(string))



'''
Output :

all for geeks

'''