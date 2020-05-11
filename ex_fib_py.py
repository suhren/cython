def get_series(n):
    a = 0
    b = 1
    result = []
    
    for _ in range(n):
        temp = a
        a = b
        b = temp + b
        result.append(a)

    return result