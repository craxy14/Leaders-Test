# # ფუნქცია რომელსაც გადაჰყავს რიცხვი ორობითი სისტემიდან ათობითში
# def decimal(num):
#     num = str(num)[::-1]
#     result = 0
    
#     for i in range(len(num)):
#         if num[i] == "1":
#             result += 2 ** i
    
#     return result
    
# print(decimal(110010))
# print(decimal(1101))
# print(decimal(10010111))

# #------------------------------------------------------------------

# # ფუნქცია რომელსაც გადაჰყავს რიცხვი ათობითი სისტემიდან ორობითში
def binary(num):
    result = ""
    
    while num > 0:
        result += str(num % 2)
        num = num // 2
    
    return result[::-1]
    
print(binary(16))

# #------------------------------------------------------------------

# # ფუნქცია რომელსაც გადაჰყავს რიცხვი ათობითი სისტემიდან რვაობითში
# def rvaobiti(num):
#     result = ""
    
#     while num > 0:
#         result += str(num % 8)
#         num = num // 8
        
#     return result
    
# print(rvaobiti(54))
# print(rvaobiti(134))

# #------------------------------------------------------------------

# # ფუნქცია რომელსაც გადაჰყავს რიცხვი რვაობითი სისტემიდან ათობითში
# def rvaobiti_to_atobiti(num):
#     num = str(num)[::-1]
#     res = 0

#     for i in range(len(num)):
#         res += (8 ** i) * int(num[i])
#     return res

# print(rvaobiti_to_atobiti(234))
# print(rvaobiti_to_atobiti(74))
# print(rvaobiti_to_atobiti(94))
# print(rvaobiti_to_atobiti(38))

# #------------------------------------------------------------------