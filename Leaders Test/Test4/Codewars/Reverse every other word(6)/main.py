def reverse_alternate(st):
    str = st.split()
    
    for i in range(len(str)):
        if i % 2 != 0:
            str[i] = str[i][::-1]
            
    result = " ".join(str)
    
    return result