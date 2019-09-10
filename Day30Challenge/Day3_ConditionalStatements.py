def conditional_statements():
    n = int(input())

    if n % 2 == 0 and (n in range(2, 5) or n > 20):
        print("Not Weird")
    else:
        print("Weird")
