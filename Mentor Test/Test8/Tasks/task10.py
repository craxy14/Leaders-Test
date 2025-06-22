# 🔟 Count Inversions in an Array
# Instructions:
#  An inversion is a pair (i,j) such that i < j and arr[i] > arr[j]. Write a function to count the number of inversions in an array using modified merge sort.
# Test Cases:
# [1,20,6,4,5] → 5
#  Inversions: (20,6), (20,4), (20,5), (6,4), (6,5)
# [2,4,1,3,5] → 3
#  Inversions: (2,1), (4,1), (4,3)
# [1,2,3] → 0
#  Array sorted ascending, no inversions.
# [3,2,1] → 3
#  Inversions: (3,2), (3,1), (2,1)

def inversions(arr):
    result = []
    for i in range(len(arr)):
        for x in range(len(arr)):
            if i < x and arr[i] > arr[x]:
                result.append((arr[i], arr[x]))
    
    return len(result)

print(inversions([1,20,6,4,5]))
print(inversions([2,4,1,3,5]))
print(inversions([1,2,3]))
print(inversions([3,2,1]))