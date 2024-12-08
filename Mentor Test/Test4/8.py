# 8. Find the Kth Smallest Element in an Array
# Task:
# Write a function that finds the k-th smallest element in an unsorted
# array.
# Test Cases:
# ● Input: arr = [3, 2, 1, 5, 6, 4], k = 2
# Output: 2
# Explanation: The 2nd smallest element in the array is 2.
# ● Input: arr = [3, 2, 1, 5, 6, 4], k = 4
# Output: 4
# Explanation: The 4th smallest element in the array is 4.
# ● Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: The 3rd smallest element in the array is 7.
# ● Input: arr = [1, 2, 3, 4, 5], k = 1
# Output: 1
# Explanation: The 1st smallest element is 1.
# ● Input: arr = [1, 2, 3, 4, 5], k = 5
# Output: 5
# Explanation: The 5th smallest element is 5.

def kth_smallest(arr, k):
    #ვასორტირებ სიას და ვაბრუნებ k ინდექსზე მდგომ ელემენტს
    return sorted(arr)[k-1]


print(kth_smallest([3, 2, 1, 5, 6, 4], 2))
print(kth_smallest([3, 2, 1, 5, 6, 4], 4))
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(kth_smallest([1, 2, 3, 4, 5], 1))
print(kth_smallest([1, 2, 3, 4, 5], 5))