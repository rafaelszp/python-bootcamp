A,B,C = input().split()

g = None

if A!=B and A!=C:
    g='A'
elif B!=A and B!=C:
    g='B'
elif C!=A and C!=B:
    g='C'
else:
    g='*'

print(g)