import math

# დავალებაში მოცემულია 5 ნორმალური სირთულის და 5 რთული დონის ალგორითმული ამოცანა.
# თითოეულ ამოცანას გააჩნია თავისი პირობა და 3 test case.

# თითოეული ამოცანისთვის უნდა შექმნათ ცალკე პითონის ან js-ის (ამ ორი ენიდან, რომლითაც გინდათ დაწერეთ ამოცანის კოდი) ფაილი და სამივე test case-ზე მიიღოთ იგივე შედეგი.
# შესაძლოა ამოცანამ მოცემულ 3 test case-ზე იგივე შედეგი დააბრუნოს, მაგრამ სხვა მაგალითებზე სწორად არ მუშაობდეს. ასეთ დროს ის შესრულებულად არ ჩაითვლება.

# !!! ყველა ამოცანას უნდა ქონდეს კომენტარები, სადაც ახსნილი იქნება კოდის რა ნაწილი რა დავალებას ასრულებს.

# !!! ამოცანების შესრულებისას დაუშვებელია browser-ის გამოყენება.


# ამოცანები:

# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.
# def first_task(arr):
#     arr = sorted(arr)

#     if len(arr) == 1:
#         return arr[0] + 1
#     else:
#         correct_arr = []
#         for i in range(arr[0], arr[-1] + 1):
#             correct_arr.append(i)

#     res = set(correct_arr) - set(arr)
#     for i in res:
#         return i

# print(first_task([2, 3, 1, 5]))






# 3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.
# def third_task(arr):
#     for i in arr:
#         if arr.count(i) == math.ceil(len(arr) / 2):
#             return i
#         else:
#             return i

# print(third_task([3, 2, 3]))









# 4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.
# 5. Given an array of integers, find all unique pairs of elements that sum to a given target number.
# def fifth_task(arr, target):
#     arr = sorted(arr)
#     result = []

#     for i in range(len(arr) - 1):
#         if arr[i] + arr[i + 1] == target:
#             result.append([arr[i], arr[i + 1]])
#     return result

# print(fifth_task([1, 2, 3, 2, 4], 5))







# 6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.
# def sixth_task(arr1, arr2):
#     return ((sum(arr1) + sum(arr2)) / (len(arr1) + len(arr2)))

# print(sixth_task([1, 2, 3], [4, 5, 6]))










# 7. Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# def sevent_task(str):
#     if str.count("(") > str.count(")"):
#         return str.count("(")
#     elif str.count("(") == str.count(")"):
#         return str.count("(") + str.count(")")
#     else:
#         return str.count(")")

# print(sevent_task("((()))"





# Test cases:
# 1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4
# 2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"
# 3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1
# 4. 0 -> 0, 5 -> 5, 10 -> 55
# 5. [1, 2, 3, 2, 4], 5 -> [(1, 4), (2, 3)],    [1, 2, 3], 7 -> [],    [-1, 0, 1, 2, -2, 3], 0 -> [(-1, 1), (-2, 2)]
# 6. [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0
# 7. "(()))())" -> 4, "((()))" -> 6, ")()())(" -> 4
# 8. [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]],    [1, 2, 3] -> [],    [0, 0, 0, 0] -> [[0, 0, 0]]
# 9. [1, 2, 3, 4] -> [24, 12, 8, 6], [0, 1, 2, 3] -> [6, 0, 0, 0], [0, 0, 1] -> [0, 0, 0]
# 10. ["eat", "tea", "tan", "ate", "nat", "bat"] -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],    ["abc", "bac", "cab"] -> [['abc', 'bac', 'cab']],    ["hello", "world", "python"] -> [['hello'], ['world'], ['python']
# the words “gum” and “mug” are anagrams because they are both three-letter words and have the same letters (g, u, and m). Let's look at some more word pairings that are anagrams: “cork” and “rock”