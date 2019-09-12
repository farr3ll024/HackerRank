def review():
    t = int(input())
    for i in range(t):
        word = input()
        print(word[::2], word[1:][::2])
