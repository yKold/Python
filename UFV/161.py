while True:
    try:
        a = input().split()
        b = int(a[0])
        c = int(a[1])

        def fatorial(a):
            res = 1
            for i in range(a):
                res*=a
                a=a-1
            return res

        if b == 0 and c != 0:
            print(1 + fatorial(c))
        elif c == 0 and b != 0:
            print(1 + fatorial(b))
        elif c != 0 and b != 0:
            print(fatorial(b) + fatorial(c))
        else:
            print(2)
            
    except EOFError:
        break