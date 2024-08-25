while True:
    try:
        x = int(input())
        vaiTer = False
        for i in range(1, 101):
            if x == i:
                vaiTer = True
        if vaiTer:
            print("vai ter duas!")
        elif x == 0:
            print("vai ter copa!")
    except EOFError:
        break