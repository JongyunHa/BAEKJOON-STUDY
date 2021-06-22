for _ in range(int(input())):
    h, w, n = map(int, input().split())

    num = n // h + 1
    floor = n % h
    if floor == 0:
        num -= 1
        floor = h
    print(floor * 100 + num)
