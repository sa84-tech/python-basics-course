def fact_rec(n):
    return n * fact_rec(n - 1) if n > 0 else 1


def fact(n):
    f = 1
    if n <= 0:
        yield f
    for i in range(1, n + 1):
        f *= i
        yield f


print('Контроль 10!:', fact_rec(10))

for el in fact(10):
    print(el, end=' ')

print('\nКонтроль 5!:', fact_rec(5))

for el in fact(5):
    print(el, end=' ')

print('\nКонтроль: 0!', fact_rec(0))

for el in fact(0):
    print(el, end=' ')
