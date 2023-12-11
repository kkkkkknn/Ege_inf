for n in range(100, 1, -1):
    s = str(bin(n)[2:])
    if n % 2 == 0:
        s += "10"
    else:
        s += "01"
    r = int(s, 2) 
    if r <= 102:
        print(r)
        break
