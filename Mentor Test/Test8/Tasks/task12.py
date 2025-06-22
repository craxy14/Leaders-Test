# 1️⃣2️⃣ Word Break Problem
# Instructions:
#  Given a string and a dictionary, determine if the string can be segmented into a space-separated sequence of dictionary words.
# Test Cases:
# "leetcode", dictionary ["leet","code"] → True
# "applepenapple", dict ["apple","pen"] → True
# "catsandog", dict ["cats","dog","sand","and","cat"] → False

def word_break(str, arr):
    res = ""
    for i in arr:
        if i not in res:
            res += i
    
    return len(res) == len(str)

print(word_break("leetcode", ["leet","code"]))
print(word_break("applepenapple", ["apple","pen"]))
print(word_break("catsandog", ["cats","dog","sand","and","cat"]))