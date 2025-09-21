# Task 8: Largest Product of Two Numbers
# Write a function max_product(nums) that returns the largest product of any two numbers in the list.
# Test Cases:
def max_product(nums):
    nums = sorted([abs(i) for i in nums])
    print(nums[-1] * nums[-2])


max_product([1,2,3,4]) # == 12
max_product([-10,-20,5,3]) # == 200
max_product([0,2]) # == 0