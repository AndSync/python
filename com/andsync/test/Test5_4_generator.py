L = [x * x for x in range(1, 11)]

print(L)

g = (x * x for x in range(1, 11))
print(g)

print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n);


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"


print(fib(10))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"


for n in fib(6):
    print(n)


def yanghui(max):
    L = [1]
    i = 0
    while i < max:
        yield L
        L = [L[0]]+ [L[n] + L[n + 1] for n in range(len(L) - 1)] + [L[-1]]
        i = i + 1
    return "done"

for l in yanghui(10):
    print(l)
