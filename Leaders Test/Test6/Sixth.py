# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

def test(word):
    word = str(word)
    result = ""

    if len(word) <= 1:
        return word
    else:
        for i in word:
            if i.isupper():
                result += "_" + i.lower()
            else:
                result += i

        final = ""
        for i in result:
            if i != " ":
                final += i

        return final[1::]

print(test("App7 Test"))

# საშინელი კოდია ik but it works :( :)