n=int(input())
lista=[float(i) for i in input().split()]
for l in lista:
    print('{:.4f}'.format(l**0.5))