# Task 5: Remove Consecutive Duplicates
# Write a function remove_consecutive_duplicates(s) that removes consecutive duplicate characters from a string.
# Test Cases:
def remove_consecutive_duplicates(str):
    res = str[0]
    
    for i in range(1, len(str)):
        if str[i] != str[i-1]:
            res += str[i]
    
    print(res)


remove_consecutive_duplicates("aaabbcddd") # == "abcd"
remove_consecutive_duplicates("hellooo") # == "helo"
remove_consecutive_duplicates("abc") # == "abc"