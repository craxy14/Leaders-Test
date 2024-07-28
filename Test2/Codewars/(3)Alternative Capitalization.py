def capitalize(s):
    odd = ""
    even = ""
    length = len(s)
    
    for i in range(length):
        if i % 2 == 0:
            even += (s[i].upper())
            odd += (s[i])
        else:
            even += (s[i])
            odd += (s[i].upper())
            
    return [even, odd]