# 1) Binary --> Decimal Conversion (2 ქულა)

# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15


def binary_to_decimal(binary):
    binary = str(binary)[::-1]
    result = 0

    for i in range(len(binary)):
        if binary[i] == "1":
            result += 1 * 2 ** i
        else:
            continue

    return result


print(binary_to_decimal(1111))