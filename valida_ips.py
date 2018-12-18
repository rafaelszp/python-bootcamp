import os.path
import sys

ips_file='ips.txt'
if not os.path.isfile(ips_file):
    print("ARQUIVO NAO ENCONTRADO")
    sys.exit(1)

with open(ips_file) as f:
    lines = f.read().splitlines()
    f.close()

validos=[]
invalidos=[]

for line in lines:
    nums = [int(i) for i in line.split('.')]
    invalido = next((n for n in nums if n > 255 or n < 0), None)
    if(invalido):
        invalidos.append(line)
    else:
        validos.append(line)
print('[Endereços válidos:]')
print('\n'.join(validos))
print('\n[Endereços inválidos:]')
print('\n'.join(invalidos))
