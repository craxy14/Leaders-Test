# 2) Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111


def decimal_to_binary(decimal):
    return bin(decimal)[2:]

print(decimal_to_binary(15))