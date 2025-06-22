# 1️⃣5️⃣ Count of Smaller Numbers After Self
# Instructions:
#  Given an array, for each element, count how many smaller elements are to its right.
# Test Cases:
# [5, 2, 6, 1] → [2, 1, 1, 0]
#  For 5 → 2 and 1 are smaller after it
#  For 2 → 1 is smaller
#  For 6 → 1 is smaller
#  For 1 → no smaller elements
# [1, 2, 3, 4] → [0, 0, 0, 0]
#  Increasing array, no smaller elements after any element
# [4, 3, 2, 1] → [3, 2, 1, 0]
#  Decreasing array, every element has all smaller elements after it
# [2, 0, 1] → [2, 0, 0]
#  2 has 0 and 1 smaller after it
#  0 and 1 have none
# [1] → [0]
#  Single element, no smaller elements after it

def smaller_count(arr):
    result = []
    count = 0
    
    for i in range(len(arr)):
        for x in range(i+1, len(arr)):
            if arr[i] > arr[x]:
                count += 1
        
        result.append(count)
        count = 0
    
    return result

print(smaller_count([5, 2, 6, 1]))
print(smaller_count([1, 2, 3, 4]))
print(smaller_count([4, 3, 2, 1]))
print(smaller_count([2, 0, 1]))
print(smaller_count([1]))