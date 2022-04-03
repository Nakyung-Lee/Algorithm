
n=int(input())

p=[]

for i in range(n):
    p.append(list(map(int,input())))


def devide(x,y,n):
    num=p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=p[i][j]:
                print("(",end='')
                devide(x, y, n // 2)
                devide(x, y + n // 2, n // 2)
                devide(x + n // 2, y, n // 2)              
                devide(x + n // 2, y + n // 2, n // 2)
                print(")",end='')
                return
    if num==1:
        print(1,end='')
    elif num==0:
        print(0,end='')

devide(0,0,n)
