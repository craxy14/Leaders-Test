# 2️⃣ Convert a List to a Dictionary
# Instructions:
#  Write a function that converts a list of key-value pair tuples into a dictionary.
# Test Cases:
# [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}
# [] → {}
# [('x', 10)] → {'x': 10}
# [('a', 1), ('a', 2)] → {'a': 2}
# [('one', 1), ('two', 2)] → {'one': 1, 'two': 2}

def list_to_dict(arr):
    result = {}
    
    for i in arr:
        result[i[0]] = i[1]
    
    return result

print(list_to_dict([('a', 1), ('b', 2)]))
print(list_to_dict([]))
print(list_to_dict([('x', 10)]))
print(list_to_dict([('a', 1), ('a', 2)]))
print(list_to_dict([('one', 1), ('two', 2)]))