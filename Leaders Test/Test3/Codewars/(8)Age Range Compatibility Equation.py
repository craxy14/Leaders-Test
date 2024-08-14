import math

def dating_range(age):
    if age <= 14:
        min = age - (0.10 * age)
        max = age + (0.10 * age)
        min = math.floor(min)
        max = math.floor(max)
        
    else:
        min = (age / 2) + 7
        max = (age - 7) * 2
        min = math.floor(min)
        max = math.floor(max)
        
    return f"{min}-{max}"