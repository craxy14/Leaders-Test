# 8️⃣ Rotate List by K Positions
# Instructions:
#  Write a function that rotates a list to the right by k positions.
# Test Cases:
# [1,2,3,4,5], 2 → [4,5,1,2,3]
# [1,2,3], 1 → [3,1,2]
# [1], 0 → [1]
# [], 3 → []
# [1,2,3,4], 4 → [1,2,3,4]

def rotate_list(arr, num):
    if len(arr) == num:
        return arr
    return arr[-num:] + arr[:-num]

print(rotate_list([1,2,3,4,5], 2))
print(rotate_list([1,2,3], 1))
print(rotate_list([1], 0))
print(rotate_list([], 3))
print(rotate_list([1,2,3,4], 4))