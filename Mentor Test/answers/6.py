def ay(str):
    splited_str = str.split(" ")
    result = ""

    for i in splited_str:
        result += i[1:] + i[0] + "ay" + " "

    return result.strip()

print(ay('Cucullus non facit monachum'))