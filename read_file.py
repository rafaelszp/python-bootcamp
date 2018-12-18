import os.path
filename='README.md'
with open(filename) as f:
    content = f.read().splitlines()

print(content,type(content))

txt = '/tmp/read_file.txt'
if not os.path.isfile(txt):
    fileh = open(txt,'w')
    fileh.writelines(content)
    fileh.close()

    with open(txt) as f2:
        content2 = f2.readlines()
        print(content2)
        f2.close()
else:
    os.remove(txt)
