def no_decimals(arr):
    if not arr:
        return True

    true_count = 0

    for i in arr:
        if i != int(i) and len(str(i)) < 3:
            return False


        if i == int(i):
            true_count += 1
        elif str(i)[2] == 0:
            true_count += 1
        else:
            return False

    return len(arr) == true_count

print(no_decimals(["-1"]))