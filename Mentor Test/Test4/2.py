# 2. Count the Number of Unique Words in a Text
# Task:
# Write a function that counts the number of unique words in a string, ignoring case sensitivity
# and punctuation.
# Test Cases:
# 1. Input: "The quick brown fox jumps over the lazy dog" → Output: 8
# 2. Input: "Hello hello world!" → Output: 2
# 3. Input: "" → Output: 0
# 4. Input: "Python is fun. Python is cool." → Output: 5
# 5. Input: "One word" → Output: 2

def unique(str):
    #გადამყავს სტრინგი პატარა ასოებათ
    str = str.lower()
    punc = ".,?!" #ვქმნი ცვლადს სადაც ვინახავ ყველა შესაძლო punctuation სიმბოლოს
    res = ""

    #for ციკლით გადავუარე სტრინგს რათა მივმწვდარიყავი თითოეულ ასოს
    for i in str:
        if i not in punc: #ვამოწმებ სტრინგის თითოეულ ასოს, თუ არ არის punc ცვლადში (რომელიც ინახავს ყველა შესაძლო punctuation სიმბოლოს)
            res += i #მაშინ დაემატოს ცარიელი სტრინგის ცვლადს

    arr = res.split() #საბოლოოდ ვაქცევ სიად
    
    return len(set(arr)) #შემდეგ ვაქცევ set-ად რათა არ იყოს duplicat-ები და ვაბრუნებ ამ set-ის სიგრძეს.

print(unique("The quick brown fox jumps over the lazy dog"))
print(unique("Hello hello world!"))
print(unique(""))
print(unique("Python is fun. Python is cool."))
print(unique("One word"))