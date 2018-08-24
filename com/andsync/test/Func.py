def my_abs(x):
    if(x>0):
        return x
    else:
        return -x

print(my_abs(-3))

def power(x,n=3):
    r=1
    while n>0:
        n=n-1
        r=r*x
    return r

print(power(2))
