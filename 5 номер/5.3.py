for n in range(1, 10000):
    a = (str(bin(n))[2:])
    s = a[:-1]
    if n % 2 != 0:
        s += '10'
    elif n % 2 == 0:
        s += '01'

    res = int(s, 2)
    if res == 2018:
        print(n)

