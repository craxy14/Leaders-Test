# 5. Encrypt and Decrypt Strings Using Caesar Cipher
# Task:
# Write a function to encrypt strings using a Caesar cipher with a given shift value.
# Pascal's Triangle is a triangular array of numbers, where each number is the sum of the two
# numbers directly above it. It represents binomial coefficients and has applications in algebra.
# Test Cases:
# 1. Input: ("abc", 2) → Output: "cde"
# 2. Input: ("xyz", 3) → Output: "abc"
# 3. Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
# 4. Input: ("Python", 0) → Output: "Python"
# 5. Input: ("abc", -1) → Output: "zab


def encrypt(str, num):
    result = ""
    #for ციკლით ვუვლი ჩვენს სტრინგს
    for i in str:
        if i.isalpha():
            #ცვლადში ვინახავ ASCII-ში კონკრეტული ასოს მნიშვნელობას დამატებული ანბანის გადასაწევი რიცხვი
            test = ord(i) + num
            #ვამოწმებ თუ ამ ასოს მნიშვნელობა მეტია z ასოს მნიშვნელობაზე, მაშინ ვაკლებ 26ს, რადგან დაიწყოს ანბანი თავიდან
            if test > ord("z"):
                test -= 26
            res = chr(test)
        result += res

    return result

print(encrypt("abc", 2))
print(encrypt("xyz", 3))
print(encrypt("Hello, World!", 5))
print(encrypt("Python", 0))
print(encrypt("abc", -1))

#-------------------------
#შემიწყალე თეზეელლლლ ||
#-------------------------