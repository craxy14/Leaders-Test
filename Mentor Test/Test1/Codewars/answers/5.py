def remove_duplicates(arr1, arr2):
    return [i for i in arr1 if i not in arr2] # ---> Final


    # return list(set(arr1) - set(arr2)) ---> Demo

print(remove_duplicates([6, -9, -1], [-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6] ))