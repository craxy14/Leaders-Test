def parts_sums(ls):
    sum1 = []
    sum2 = 0
    
    for i in reversed(ls):
        sum2 += i
        sum1.append(sum2)
        
    sum1.reverse()
    sum1.append(0)
    
    return sum1