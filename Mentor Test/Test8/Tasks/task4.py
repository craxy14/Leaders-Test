# 4️⃣ Implement a Simple Caesar Cipher
# Instructions:
#  Write a function that takes a message and a shift value and returns the message with each letter shifted (A→B, B→C, etc). Ignore non-alphabet characters.
# Test Cases:
# "abc", 1 → "bcd"
# "xyz", 2 → "zab"
# "Hello!", 3 → "Khoor!"
# "ABC", 1 → "BCD"
# "Test 123", 4 → "Xiwx 123"

def caesar_cipher(str, shift):
    alph = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for i in str:
        if i in alph and i.isupper() and i.isalpha():
            if alph.index(i) + shift <= len(alph):
                result += alph[(alph.index(i) + shift) % 26].upper()
            else:
                result += alph[(alph.index(i) + shift) % 26].upper()

        elif i in alph and not i.isupper() and i.isalpha():
            if alph.index(i) + shift <= len(alph):
                result += alph[(alph.index(i) + shift) % 26].upper()
            else:
                result += alph[(alph.index(i) + shift) % 26].upper()
        else:
            result += i
    
    return result

print(caesar_cipher("abc", 1))
print(caesar_cipher("xyz", 2))
print(caesar_cipher("Hello", 3))
print(caesar_cipher("ABC", 1))
print(caesar_cipher("Test 123", 4))