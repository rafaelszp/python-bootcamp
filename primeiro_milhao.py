'''
A primeira linha da entrada contém um número inteiro
N
, que indica o número de dias que a lista contém. Cada uma das linhas seguintes contém um único inteiro
A
, o número de acessos em um dia. O primeiro número dado indica o número de acessos no primeiro dia, o segundo número
dado indica o número de acessos no segundo dia, e assim por diante.

Saída
Seu programa deve escrever na saída uma única linha, contendo um único número inteiro, o número de dias que foram
necessários para a soma dos acessos à pagina de Alice e Bia chegar a 1000000.
'''

n=int(input())

vis=[]
dia=None
for i in range(n):
    a=int(input())
    vis.append(a)
total = 0
for i,v in enumerate(vis):
    total+=v
    if(total>=1000000 and dia):
        dia=i+1
print(dia)