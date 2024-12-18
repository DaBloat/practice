def hanoi(n, start, end, mid):
    if n==1:
        print(f"ring {n} from {start} to {end}")
        return
    hanoi(n-1, start, mid, end)
    print(f"ring {n} from {start} to {end}")
    hanoi(n-1, mid, end, start)

hanoi(20, 'A', 'C', 'B')
