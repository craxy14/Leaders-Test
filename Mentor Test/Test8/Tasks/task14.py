# 1️⃣4️⃣ Maximum XOR of Two Numbers in an Array
# Instructions:
#  Find two numbers in an array that yield the maximum XOR value.
# Test Cases:
# [3, 10, 5, 25, 2, 8] → 28
#  Max XOR between 5 and 25: 5 ^ 25 = 28
# [0] → 0
#  Only one number, XOR is 0
# [2, 4] → 6
#  2 ^ 4 = 6
# [8, 10, 2] → 10
#  8 ^ 2 = 10
# [12, 15, 7, 9] → 15
#  12 ^ 3 = 15 (or 15 ^ 0)

def max_xor(arr):
    maximum = 0
    
    for i in arr:
        for x in range(1, len(arr)):
            if i ^ arr[x] > maximum:
                maximum = i ^ arr[x]
    
    return maximum

print(max_xor([3, 10, 5, 25, 2, 8]))
print(max_xor([0]))
print(max_xor([2, 4]))
print(max_xor([8, 10, 2]))
print(max_xor([12, 15, 7, 9]))