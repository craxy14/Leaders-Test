#  1.Check If Two Strings Are Anagrams
#  Task:
#  Write a function that determines if two strings are anagrams of eachother.
#  TestCases:
#  1. Input:("listen","silent")→Output:True
#  2. Input:("triangle","integral")→Output:True
#  3. Input:("apple","pale")→Output:False
#  4. Input:("a","a")→Output:True
#  5. Input:("rat","car")→Output:False

def anagrams(str1, str2):
    return sorted(str1) == sorted(str2) #ვამოწმებ თუ დასორტირებული სტრინგები არიან ერთმანეთის იდენტურები გამოდის რომ ისინი არიან ერთმანეთის ანაგრამები

print(anagrams("listen", "silent"))
print(anagrams("triangle", "integral"))
print(anagrams("apple", "pale"))
print(anagrams("a", "a"))
print(anagrams("rat", "car"))