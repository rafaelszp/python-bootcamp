S=input()[:50].lower()
vogais=['a','e','i','o','u']
seq=''
for s in S:
    for v in vogais:
        seq=seq + (v if v==s else '')
print('S' if seq==seq[::-1] else 'N')