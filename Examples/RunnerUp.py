def runner_up():
    n = int(input())
    arr = map(int, input().split())
    get_runner_up(n, arr)

# inline
def get_runner_up(n, arr):
    return sorted(list(dict.fromkeys(arr)))[-2]

# O(n) time
def efficient_get_runner_up(n, arr):
    pass

