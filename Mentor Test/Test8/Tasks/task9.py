# 9️⃣ Find Longest Palindromic Substring
# Instructions:
#  Write a function that finds the longest palindromic substring in a given string.
# Test Cases:
# "babad" → "bab" or "aba"
# "cbbd" → "bb"
# "a" → "a"
# "" → ""
# "forgeeksskeegfor" → "geeksskeeg"

def longest_palindrome(str):
    result = ""
    while result == result[::-1]:
        for i in str:
            result += i

    return result

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome(""))
print(longest_palindrome("forgeeksskeegfor"))