# Test Cases:
# ● Input: n = 5
# Output: 30
# Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product
# is 2 * 3 * 5 = 30.
# ● Input: n = 10
# Output: 210
# Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their
# product is 2 * 3 * 5 * 7 = 210.
# ● Input: n = 1
# Output: 1
# Explanation: There are no primes less than or equal to 1, so the primorial is 1 by
# definition.
# ● Input: n = 7
# Output: 210
# Explanation: The prime numbers less than or equal to 7 are 2, 3, 5, and 7. Their
# product is 2 * 3 * 5 * 7 = 210.
# ● Input: n = 11
# Output: 2310
# Explanation: The prime numbers less than or equal to 11 are 2, 3, 5, 7, and 11. Their
# product is 2 * 3 * 5 * 7 * 11 = 2310.
import math


def prime(num):
    #for ციკლს გადავცემ დიაპაზონს 2, დამრგვალებული გადაცემული რიცხვის ფესვს დამატებული ერთამდე
    for i in range(2, int(math.sqrt(num)) + 1):
        # ვამოწმებ თუ რიცხვის საიტერაციო ცვლადზე გაყოფის შედეგად ნაშთი მრჩება 0, მაშინ რიცხვი არ არის მარტივი
        if num % i == 0:
            return False
    #სხვა შემთხვევაში რიცხვი გამოდის მარტივი
    return True

def primoral(num):
    res = 1
    #ვქმნი რიცვების დიაპაზონს 2დან ჩვენი გადმოცემული რიცხვის ჩათვლით
    for i in range(2,num + 1):
        #ვიძახებ prime ფუნქციას და ვამოწმებ არის თუ არა რიცხვი მარტივი
        if prime(i):
            res *= i #თუ ჩვენი შედარება True-ს დააბრუნებს, მაშინ ჩვენი შედეგის ჯამს ვამრავლებ და მის მნიშვნელობას ვანახლებ ამ მარტივ რიცხვზე
    return res

print(primoral(5))
print(primoral(10))
print(primoral(1))
print(primoral(7))
print(primoral(11))