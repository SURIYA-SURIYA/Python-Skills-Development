#Longest common prefix


def longest_common_prefix(strs):
    # If the list is empty, return "-1"
    if not strs:
        return "-1"

    # Sort the list of strings
    strs.sort()

    # Get the first and last strings after sorting
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))

    i = 0
    # Find the common prefix between the first
    # and last strings
    while i < min_length and first[i] == last[i]:
        i += 1

    # Check if there's no common prefix
    if i == 0:
        return "-1"

    # Return the common prefix
    return first[:i]

strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("The longest common prefix is:",
      longest_common_prefix(strs))

'''
Output
The longest common prefix is: gee

'''