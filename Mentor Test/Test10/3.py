# Task 3: Remove Punctuation
# Write a function remove_punctuation(s) that removes all punctuation characters from a string.
# Test Cases:
def remove_punctuation(str):
    print("".join([i for i in str if i == " " or i.isalpha()]))


remove_punctuation("Hello, world!") # == "Hello world"
remove_punctuation("Python: easy? Yes!") # == "Python easy Yes"