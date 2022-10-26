def f(n):
    if(n<=1):
        return 1
    else:
        return n*(f(n-1))

def f_fwd(i, n):
    if(i <= 0 or n<= 0):
        return 1
    elif(i >= n):
        return n
    else:
        return i*f_fwd(i+1, n)

x = f_fwd(1, 4)
y = f(4)
print(y)
print(x)