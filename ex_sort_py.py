def sort(x):
    x = x.copy()
    n = len(x)
    for i in range(n):
        for j in range(i, n):
            if x[i] > x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x