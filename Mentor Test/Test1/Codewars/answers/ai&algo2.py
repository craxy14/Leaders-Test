def capitalize_count(str):
    count = 0

    for i in str:
        if i.isupper():
            count += 1

    return count
print(capitalize_count("Hello World!"))

#this function uses one built in function .isupper(), in this case it does one comperasion / fewest number we can get as a result is 0 and the maximum number of capitalized characters we can get is: n --> len(str)