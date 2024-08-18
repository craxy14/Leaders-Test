def is_divisible(first, *others):
    
    for i in others:
        if first % i != 0:
            return False
        
    return True