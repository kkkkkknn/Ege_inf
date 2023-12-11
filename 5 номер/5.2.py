for n in range(1, 100):
    b = int(str(bin(n))[2:])
    s = f"{b}"
    if n % 2 == 0:
        s += "01"
    else:
        s += "10"
    if int(s, 2) > 102:
        print(int(s, 2))
        break
