# 3. Reverse the Order of Words in a Sentence
#  Task:
#  Write a function that takes a sentence and reverses the order of its words.
#  Test Cases:
#  1. Input: "Hello World" → Output: "World Hello"
#  2. Input: "Python is great" → Output: "great is Python"
#  3. Input: "a b c" →Output: "c b a"
#  4. Input: "" → Output: ""
#  5. Input: " Spaces " → Output: "Spaces"

def rev_order(str):
    #ვაქცევ სტრინგს სიად, თითოეული სიტყვა არის სიის ელემენტი
    word_arr = str.split()
    res = ""

    #for ციკლით გადავუარე სიტყვების სიას ბოლოდან დასაწყისამდე
    for i in word_arr[::-1]:
        res += " " + i

    #strip ფუნქციას თუ არგუმენტს არ გადავცემთ, თავში და ბოლოში აშორებს space-ებს
    return res.strip()

print(rev_order("Hello World"))
print(rev_order("Python is great"))
print(rev_order("a b c"))
print(rev_order(""))
print(rev_order(" Spaces "))