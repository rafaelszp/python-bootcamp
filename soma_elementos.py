"""
Nesse problema você receberá um conjunto de valores e sua tarefa é imprimir a soma desses valores.

Entrada
A entrada consiste em duas linhas. A primeira linha possui apenas um valor N
, representando a quantidade de valores que você deve ler. A segunda linha possui N números inteiros separados
por um espaço em branco.

Saída
Você deve imprimir a soma dos N
 números inteiros lidos na entrada.

Restrições
1
≤
N
≤
100
"""

n=int(input())
numeros= [int(i) for i in input().split()]

total=0
for num in numeros:
    total+=num
print(total)

