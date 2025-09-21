# Task 4: Intersection of Two Dictionaries
# Write a function dict_intersection(d1, d2) that returns a dictionary containing keys that appear in both dictionaries, with their values summed.
# Test Cases:
def dict_intersection(dict1, dict2):
    res = {}

    for i in dict1:
        if i in dict2:
            res[i] = dict1[i] + dict2[i]

    print(res)

dict_intersection({"a":1,"b":2},{"b":3,"c":4}) # == {"b":5}
dict_intersection({"x":10},{"y":5}) # == {}