def solution(array_a, array_b):
    sum = 0
    
    for i in range(len(array_a)):
        diff = array_a[i] - array_b[i]
        square = diff ** 2
        sum += square
        
    avarage = sum / len(array_a)
    
    return avarage