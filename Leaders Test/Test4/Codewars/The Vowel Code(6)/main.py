def encode(st):
    result = ""
    char_num = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}
    
    for i in st:
        if i not in char_num:
            result += i
        else:
            result += char_num[i]
            
    return result
    
def decode(st):
    result = ""
    
    char_num = {"1":"a", "2":"e", "3":"i", "4":"o", "5":"u"}
    
    for i in st:
        if i not in char_num:
            result += str(i)
        else:
            result += char_num[i]
    
    return result