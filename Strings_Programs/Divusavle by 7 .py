

# Python program to check whether a number is divisible by 7
 
# Function to check whether a number is divisible by 7
def isDivisibleBy7(num) :
     
    # If number is negative, make it positive
    if num < 0 :
        return isDivisibleBy7( -num )
 
    # Base cases
    if( num == 0 or num == 7 ) :
        return True
     
    if( num < 10 ) :
        return False
         
    # Recur for ( num / 10 - 2 * num % 10 ) 
    return isDivisibleBy7( num // 10 - 2 * ( num - num // 10 * 10 ) )
     
# Driver program
num = 616
if(isDivisibleBy7(num)) :
    print ("Divisible")
else :
    print ("Not Divisible")
 
# This code is contributed by Nikita Tiwari
'''

Output

Divisible

'''