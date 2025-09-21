# Task 2: Decode Run-Length Encoding
# Write a function decode_rle(s) that decodes a run-length encoded string.
#  Example: "a3b2c1" → "aaabbc"
# Test Cases:
def decode_rle(str):
    print("".join([str[i-1] * int(str[i]) for i in range(len(str)) if i % 2 == 1]))

    # result = ""
    
    # for i in range(len(str)):
    #     if i % 2 == 1:
    #         result += str[i-1] * int(str[i])
    
    # print(result)


decode_rle("a3b2c1") # == "aaabbc"
decode_rle("x5y1") # == "xxxxxy"
decode_rle("") # == ""