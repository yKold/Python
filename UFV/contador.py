def Contador():
    B = len(A)
    C = []
    for i in range(B):
        C.append(A[B-(i + 1)])
        i+=i
        print(C)
    
def Contador(A):
    B = 0
    if A > 99:
        B = A/100
        C.append(B)
        A = A%100
        if A > 49:
            B = A/50
            C.append(B)
            A = A%50
            if A > 19:
                B = A/20
                C.append(B)
                A = A%20
                if A > 9:
                    B = A/10
                    C.append(B)
                    A = A%10
                    if A > 4:
                        B = A/5
                        C.append(B)
                        A = A%5
                        if A > 1:
                            B = A/2
                            C.append(B)
                            A = A%2
                            if A == 1:
                                B = 1
                                C.append(B)
                                A = 0
                                print(B)
                                print(A)
    if A > 49:
        B = A/50
        C.append(B)
        A = A%50
        if A > 19:
            B = A/20
            C.append(B)
            A = A%20
            if A > 9:
                B = A/10
                C.append(B)
                A = A%10
                if A > 4:
                    B = A/5
                    C.append(B)
                    A = A%5
                    if A > 1:
                        B = A/2
                        C.append(B)
                        A = A%2
                        if A == 1:
                            B = 1
                            C.append(B)
                            A = 0
                            print(B)
                            print(A)
    if A > 19:
        B = A/20
        C.append(B)
        A = A%20
        if A > 9:
            B = A/10
            C.append(B)
            A = A%10
            if A > 4:
                B = A/5
                C.append(B)
                A = A%5
                if A > 1:
                    B = A/2
                    C.append(B)
                    A = A%2
                    if A == 1:
                        B = 1
                        C.append(B)
                        A = 0
                        print(B)
                        print(A)
    if A > 9:
        B = A/10
        C.append(B)
        A = A%10
        if A > 4:
            B = A/5
            C.append(B)
            A = A%5
            if A > 1:
                B = A/2
                C.append(B)
                A = A%2
                if A == 1:
                    B = 1
                    C.append(B)
                    A = 0
                    print(B)
                    print(A)
    if A > 4:
        B = A/5
        C.append(B)
        A = A%5
        if A > 1:
            B = A/2
            C.append(B)
            A = A%2
            if A == 1:
                B = 1
                A = 0
                print(B)
                print(A)
    if A > 1:
        B = A/2
        C.append(B)
        A = A%2
        if A == 1:
            B = 1
            C.append(B)
            A = 0
            print(B)
            print(A)
    if A == 1:
        B = 1
        C.append(B)
        A = 0
        print(B)
        print(A)