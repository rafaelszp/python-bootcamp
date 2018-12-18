def eh_primo(x):
    if(x % 2==0):
        return False
    elif x==2:
        return True
    elif x<=1:
        return False
    else:
        half=x//2;
        for h in range(1,half+1):
            if h==1:
                continue
            #print(x,h,str(x%h))
            if x % h == 0:
                return False
        return True

x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')