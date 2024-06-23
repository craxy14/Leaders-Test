def min_sum(arr):
    arr.sort()
    sum = 0
    
    for i in range(len(arr) // 2):
        sum += arr[i] * arr[-1 - i]
        
    return sum