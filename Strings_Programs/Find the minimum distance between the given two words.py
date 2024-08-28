#Find the minimum distance between the given two words

# Python3 code to implement the approach
 
# Function to return shortest distance
def shortestDistance(s, word1, word2) :
 
    d1 = -1; d2 = -1;
    ans = 100000000;
 
    # Traverse the string
    for i in range(len(s)) :
        if (s[i] == word1) :
            d1 = i;
        if (s[i] == word2) :
            d2 = i;
        if (d1 != -1 and d2 != -1) :
            ans = min(ans, abs(d1 - d2));
 
    # Return the answer
    return ans;
 
# Driver Code
if __name__ == "__main__" :
 
    S = [ "the", "quick", "brown", "fox", "quick" ];
 
    word1 = "the"; word2 = "fox";
 
    # Function Call
    print(shortestDistance(S, word1, word2));
 
   # This code is contributed by AnkThon
'''
Output

3
'''