# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False


def check_palindrome(word):
    res = ""

    for i in word:
        if i.isalnum():
            res += i.lower()
        
    return res == res[::-1]


print(check_palindrome("A man a plan a canal Panama"))