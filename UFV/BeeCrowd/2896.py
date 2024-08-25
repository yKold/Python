t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    g = n//k
    resto = n%k
    print(g+resto)