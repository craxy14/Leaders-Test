#So Many Permutations!

# def permutations(s):
#     if len(s) <= 1:
#         return [s]
    
#     result = []
    
#     for i in range(len(s)):
#         for x in permutations(s[0:i] + s[i + 1:]):
#             result.append(s[i] + x)
            
#     return list(set(result))