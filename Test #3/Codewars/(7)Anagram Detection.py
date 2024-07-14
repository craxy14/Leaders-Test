# def is_anagram(test, original):
#     test = test.lower()
#     original = original.lower()
    
#     sorted_test = sorted(test)
#     sorted_original = sorted(original)
    
#     return sorted_test == sorted_original


def luck_check(st):
    try:
        length = len(st)
        mid = length // 2

        if length % 2 == 0:
            left = st[:mid]
            right = st[mid:]

        else:
            left = st[:mid]
            right = st[mid + 1:]

        sum_left = 0
        for i in left:
            sum_left += int(i)

        sum_right = 0
        for i in right:
            sum_right += int(i)
            
        return sum_left == sum_right
    
    except:
        raise ValueError

luck_check()