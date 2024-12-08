# 7. Find All Prime Numbers in a Given Range
# Task:
# Write a function that takes two integers, start and end, and returns
# a list of all prime numbers in the range [start, end]. A prime
# number is a number greater than 1 that has no divisors other than 1
# and itself.
# Test Cases:
# ● Input: start = 10, end = 20
# Output: [11, 13, 17, 19]
# ● Input: start = 1, end = 10
# Output: [2, 3, 5, 7]
# ● Input: start = 20, end = 30
# Output: [23, 29]
# ● Input: start = 24, end = 25
# Output: []
# ● Input: start = 1, end = 1
# Output: []


#ვაიმპორტებ math ბიბლიოთეკას
import math

#ვქმნი ფუნქციას რომელსაც გადაეცემა რიცხვი და ამოწებს არის თუ არა ეს კონკრეტული რიცხვი მარტივი
def prime(num):
    #for ციკლს გადავცემ დიაპაზონს 2, დამრგვალებული გადაცემული რიცხვის ფესვს დამატებული ერთამდე
    for i in range(2, int(math.sqrt(num)) + 1):
        # ვამოწმებ თუ რიცხვის საიტერაციო ცვლადზე გაყოფის შედეგად ნაშთი მრჩება 0, მაშინ რიცხვი არ არის მარტივი
        if num % i == 0:
            return False
    #სხვა შემთხვევაში რიცხვი გამოდის მარტივი
    return True

#ვქმნი ფუნქციას, რომელსაც გადაეცემა ორი არგუმენტი, დასაწყისი წერტილი და დასასრული
def prime_range(start, stop):
    #ვქმნი საბოლოო შედეგის ცარიელ სიას
    res = []
    #for ციკლით შევქმენი რიცხვების თანმიმდევრობა გადაცემულ დიაპაზონში
    for i in range(start, stop + 1):
        #ვამოწმებ და ვიძახებ prime ფუნქციას, რომელსაც გადავცემ საიტერაციო ცვლადს (რიცხვს) და ამოწმებს არის თუ არა ეს რიცხვი მარტივი
        if prime(i):
            res.append(i) #თუ ზემოთ if დააბრუნებს True-ს მაშინ სიაში ჩაემატება ეს კონკრეტული რიცხვი
    
    return res
print(prime_range(10, 20))
print(prime_range(1, 10))
print(prime_range(20, 30))
print(prime_range(24, 25))
print(prime_range(1, 1))