# 1️⃣3️⃣ Maximum Product Subarray
# Instructions:
#  Find the contiguous subarray within an array which has the largest product.
# Test Cases:
# [2,3,-2,4] → 6
# [-2,0,-1] → 0
# [0,-3,1,-2] → 1

def largest_product(arr):
    largest = 0
    
    for i in range(len(arr)-1):
        if largest < arr[i] * arr[i + 1]:
            largest = arr[i] * arr[i + 1]
    return largest

print(largest_product([2,3,-2,4]))
print(largest_product([-2,0,-1]))
print(largest_product([0,-3,1,-2]))