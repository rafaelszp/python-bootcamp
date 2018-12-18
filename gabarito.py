n=int(input())
gab=input()
res=input()

corretas=0
for i,g in enumerate(gab):
    corretas = corretas + (1 if g==res[i] else 0)

print(corretas)