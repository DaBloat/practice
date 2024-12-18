def sum_of_square1s(n):
    # SLOW AS SHIT
    total = n
    lengths = []
    squares = []
    for i in range(1, int(n ** 0.5) + 1):
        squares.append(i*i)
    while len(squares) != 0:
        main = squares[-1]
        addends = []
        total -= main
        addends.append(main)
        while total != 0:
            for i in squares[::-1]:
                if total - i >= 0:
                    addends.append(i)
                    total -= i
        total = n
        squares.pop()
        lengths.append(len(addends))

    return min(lengths)    


def sum_of_squares(n):
    if n ** 0.5 == int(n ** 0.5):
        return 1
    c1 = 0
    while n & 3 == 0:
        n >>= 2
        c1 += 1
    if n & 7 == 7:
        return 4
    for i in range(1, int(n ** 0.5) + 1):
        if (n - i * i) ** 0.5 == int((n - i * i) ** 0.5):
            return 2
    return 3
        
print(sum_of_squares(18))
