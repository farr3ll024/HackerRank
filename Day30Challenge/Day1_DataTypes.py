def data_types():
    i = 4
    d = 4.0
    s = 'HackerRank '
    default_parms = [i, d, s]

    parms = get_input()
    run_ops(parms, default_parms)

def get_input():
    input_params = []
    for x in range(3):
        input_params.append(input())
    return input_params

def run_ops(parms, default_parms):
    i = 0
    for parm, default_parm in zip(parms, default_parms):
        if i == 0:
            print(int(parm) + default_parm)
            i += 1
            continue
        elif i == 1:
            print(float(parm) + default_parm)
            i += 1
        else:
            print(default_parm + str(parm))
            i += 1
            continue


