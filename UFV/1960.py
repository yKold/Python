x = int(input())
res = []
while x > 0:
    if x >= 1000:
        res.append("M")
        x -= 1000
    elif x >= 900:
        res.append("CM")
        x -= 900
    elif x >= 500:
        res.append("D")
        x -= 500
    elif x >= 400:
        res.append("CD")
        x -= 400
    elif x >= 100:
        res.append("C")
        x -= 100
    elif x >= 90:
        res.append("XC")
        x -= 90
    elif x >= 50:
        res.append("L")
        x -= 50
    elif x >= 40:
        res.append("XL")
        x -= 40
    elif x >= 10:
        res.append("X")
        x -= 10
    elif x >= 9:
        res.append("IX")
        x -= 9
    elif x >= 5:
        res.append("V")
        x -= 5
    elif x >= 4:
        res.append("IV")
        x -= 4
    elif x >= 1:
        res.append("I")
        x -= 1
print("".join(res))