# Task 7: Subset Sum Check
# Write a function has_subset_sum(nums, target) that returns True if any subset of numbers adds up to target.
# Test Cases:
def has_subset_sum(nums, target):
    if not nums:
        return True
    
    for i in nums:
        for x in range(1, len(nums)):
            if i + nums[x] == target:
                return True

    return False


print(has_subset_sum([3,34,4,12,5,2], 9)) # == True  # 4+5
print(has_subset_sum([3,34,4,12,5,2], 30)) # == False
print(has_subset_sum([], 0)) # == True