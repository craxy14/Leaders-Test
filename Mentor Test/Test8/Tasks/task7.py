# 7️⃣ Find Pairs with Given Sum
# Instructions:
#  Write a function that returns all pairs of numbers from a list that add up to a given target sum.
# Test Cases:
# [1,2,3,4], 5 → [(1,4),(2,3)]
# [0,0,1,1], 1 → [(0,1),(0,1)]
# [5,5,5], 10 → [(5,5),(5,5),(5,5)]
# [1], 2 → []
# [], 0 → []

def sum_pairs(arr, target):
    result = []
    
    for i in range(len(arr)):
        for x in range(2, len(arr)):
            if arr[i] + arr[x] == target:
                result.append((arr[i], arr[x]))
    
    return result

print(sum_pairs([1,2,3,4], 5))
print(sum_pairs([0,0,1,1], 1))
print(sum_pairs([5,5,5], 10))
print(sum_pairs([1], 2))
print(sum_pairs([], 0))