N,M=map(int,input().split())

if N==1:
    print(1)
elif N==2:
    if M>7:
        print(4)
    else:
        print((M+1)//2)
elif N>=3:
    if M<7:
        if M<=3:
            print(M)
        else:
            print(4)
    else:
        print(M-2)
