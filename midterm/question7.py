def fact(n):
    res = 1
    for i in range(n):
        res = res*(i+1)
    return res

x = fact(5)
print(x)