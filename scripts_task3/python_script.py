def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-10+1):
            out *= i
    else:
        lim = n - 20
        out = 0
        for i in range(1, lim+1):
            out += i
    print(out)


n = int(input("Enter an integer: "))
compute(n)
