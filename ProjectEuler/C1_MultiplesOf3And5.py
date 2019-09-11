def sum_multiples():
    get_input()


def get_input():
    cases = []
    t = int(input().strip())
    for a0 in range(t):
        cases.append(float(input().strip()))

    for c0 in cases:
        calculate_sum(c0)


def calculate_sum(n):
    print(sum([b for b in range(3, n) if (b % 3 == 0 or b % 5 == 0)]))
