

def mutate_string(s, i, c):
    new_s = list(s)
    new_s[i] = c
    s = ''.join(new_s)
    return s    


