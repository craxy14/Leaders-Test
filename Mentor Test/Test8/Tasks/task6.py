# 6️⃣ Sum Numbers in a String
# Instructions:
#  Write a function that finds all numbers in a string and returns their sum.
# Test Cases:
# "abc123xyz" → 123
# "7 apples and 3 oranges" → 10
# "no numbers" → 0
# "1a2b3c" → 6
# "100 200" → 300

def sum_numbers(str):
    alph = "abcdefghijklmnopqrstuvwxyz"
    str = str.lower()
    
    for i in alph:
        if i in str:
            str = str.replace(i, " ")

    splited_str = str.split()
    return sum([int(i) for i in splited_str])

print(sum_numbers("abc123xyz"))
print(sum_numbers("7 apples and 3 oranges"))
print(sum_numbers("no numbers"))
print(sum_numbers("1a2b3c"))
print(sum_numbers("100 200"))