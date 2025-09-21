# Task 10: Longest Consecutive Characters
# Write a function longest_consecutive_char(s) that returns the longest run of the same character.
# Test Cases:
def longest_consecutive_char(str):
    if not str:
        return "", 0
    
    result = []
    test = str[0]

    for i in str[1:]:
        if i == test[-1]:
            test += i
        else:
            result.append(test)
            test = i

    result.append(test)
    
    return sorted(result, key=len)[-1][-1], len(sorted(result, key=len)[-1])


print(longest_consecutive_char("aaabbbaaac")) # ("a",3)
print(longest_consecutive_char("bbbbb")) # ("b",5)
print(longest_consecutive_char("")) # ("",0)