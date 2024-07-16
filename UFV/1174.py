# x = [float(i) for i in range(100)]
# x[0] = 0
# for i in range(len(x)):
#     try:
#         y = float(input())
#         if y <= 10:
#             x[i+1] = y
#         else:
#             while y > 10:
#                 y = float(input())
#             x[i+1] = y
#         print(f"A[{i+1}] = {y}")
#     except EOFError:
#         print("Entrada não disponível. O programa será encerrado.")
#         break

A = []

for i in range(100):

    num = A.append(float(input()))

    if A[i] <= 10:

        print(f"A[{i}] = {A[i]:.1f}")