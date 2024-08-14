def outlier(arr):
    odd_count = 0
    even_count = 0

    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count > even_count:
        return [i for i in arr if i % 2 == 0][0]
    else:
        return [i for i in arr if i % 2 != 0][0]


print(outlier([-4207752, 362590, 5205484, 11340, 3740336, 1360605]))