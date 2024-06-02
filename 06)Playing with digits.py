#Playing with digits :

# def dig_pow(n, p):
#     str_n = str(n)
    
#     result = 0
    
#     for i in range(len(str_n)):
#         sum = p + i
        
#         int_digit = int(str_n[i])
#         result += int_digit ** sum
        
#     if result % n == 0:
#         return result / n
    
#     else:
#         return -1