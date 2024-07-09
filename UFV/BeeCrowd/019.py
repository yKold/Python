from math import floor
N = int(input())
if N <= 3600:
    Hora = floor(0)
    Min = floor(N/60)
    Sec = floor(N%60)
    print("{:.0f}:{:.0f}:{:.0f}".format(Hora, Min, Sec))
else:
    Hora = floor(N/60/60)
    Min = floor(N/60%60)
    Sec = floor(N%60)
    print("{:.0f}:{:.0f}:{:.0f}".format(Hora, Min, Sec))