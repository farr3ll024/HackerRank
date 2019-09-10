def operators():
    payment = []
    for x in range(3):
        payment.append(input())

    # print(calculate_meal_cost(payment))
    print(solve(payment[0], payment[1], payment[2]))


def calculate_meal_cost(payment):
    tip = float(payment[0]) * (float(payment[1]) / 100)
    tax = float(payment[0]) * (float(payment[2]) / 100)
    total_cost = float(payment[0]) + tip + tax

    return int(total_cost)


def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost) * (float(tip_percent) / 100)
    tax = float(meal_cost) * (float(tax_percent) / 100)
    return int(round(float(meal_cost) + tip + tax))
