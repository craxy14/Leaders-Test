# 8) Orders (4 ქულა)

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# NOTE: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples:
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4 of Fo1r people g3ood th5e the2"  -->  "Fo1r the2 g3ood 4 of th5e people"
# ""  -->  ""

def test(sentance):
    num = "123456789"
    sentance = sentance.split()
    result = []

    for i in range(1, len(sentance) + 1):
        for x in sentance:
            if str(i) in x:
                result.append(x)

    return result

print(test("is2 Thi1s T4est 3a"))