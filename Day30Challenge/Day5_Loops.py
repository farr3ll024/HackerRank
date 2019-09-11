def loops():
    n = int(input())
    for i in range(1, 11):
        text = str(n) + " x " + str(i) + " = " + str(n * i)
        print(text.strip('\n')),
