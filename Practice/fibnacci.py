def fib1(num):
    # Slow ways to take the fibonnacci, even negatives
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num > 0:
        return fib(num - 1) + fib(num - 2)
    if num < 0:
        return fib(num + 2) - fib(num + 1)

def calc(num):
    if num == 0:
        return (0, 1)
    elif num == 1:
        return (1, 1)
    else:
        a, b = calc(num // 2)
        p = a * (2 * b - a)
        q = b * b + a * a
        return (p, q) if num % 2 == 0 else (q, p + q)

def fib(num):
    # can get even the millionth fibonacci
    if num >= 0:
        return calc(num)[0]
    else:
        return -calc(-num)[0] if num % 2 ==0 else calc(-num)[0]


print(fib(5))
