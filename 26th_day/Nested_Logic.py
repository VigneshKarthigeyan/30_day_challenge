# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_days(a, b):
    # actual-return,expected-returned
    if a[2] > b[2]:
        return 10000
    elif a[2] == b[2]:
        if a[1] == b[1] and a[0] > b[0]:
            return 15 * (a[0] - b[0])
        elif a[1] > b[1]:
            return 500 * (a[1] - b[1])
    return 0


a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
ret = count_days(a, b)
print(ret)
