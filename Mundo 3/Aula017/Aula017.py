num = [1,2,3,4,5]

num.append(10)
num.append(99)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(1)
num.remove(5)

for i in num:
    print(i)