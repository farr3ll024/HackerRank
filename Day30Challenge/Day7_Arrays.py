def arrays():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
