def lcm(*args):
    if not args:
        return 1
    
    result = 0
    
    for i in args:
        result *= i
            
    return result