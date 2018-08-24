def f(x):
 return x*x;

r=map(f,[1,2,3,4])

print(list(r))

print(list(map(str,[1,2,3,4,5])))

from functools import  reduce
def add(x,y):
    return x+y;
print(reduce(add,[1,2,3,4,5]))


