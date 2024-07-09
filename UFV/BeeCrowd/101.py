# entrada = input().split()
# M = int(entrada[0])
# N = int(entrada[1])

# def Analise(M, N):
#     O = max(M, N)
#     P = min(M, N)
#     Val = []
#     Sum = 0
#     if O > P and O + P != O and O + P != 0:
#         for i in range(O-P+1):
#             Val.append(P+i)
#         for i in range(len(Val)):
#             Sum += Val[i]
#         print("{} Sum={}".format(str(Val)[1:-1].replace(",", ""), Sum))
#     elif M == 0 and N == 0:
#         return 0
#     if not M == 0 or not N == 0:
#         entrada = input().split()
#         M = int(entrada[0]) 
#         N = int(entrada[1])
#         return Analise(M, N)
# Analise(M, N)

def Inputzadas():
    entrada = input().split()
    M = int(entrada[0])
    N = int(entrada[1])
    Val = []
    Sum = 0

    if M > N and M + N != M and M + N != 0:
        for i in range(M-N+1):
            Val.append(N+i)
        for i in range(len(Val)):
            Sum += Val[i]
        print("{} Sum={}".format(str(Val)[1:-1].replace(",", ""), Sum))

    elif M < N and M + N != N and M + N != 0:
        for i in range(N-M+1):
            Val.append(M+i)
        for i in range(len(Val)):
            Sum += Val[i]
        print("{} Sum={}".format(str(Val)[1:-1].replace(",", ""), Sum))
    else:
        return 0

    if not M == 0 or not N == 0:
        return Inputzadas()

Inputzadas()
