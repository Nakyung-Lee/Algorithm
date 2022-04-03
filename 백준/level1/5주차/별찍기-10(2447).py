n=int(input())

def three(x,y,n):
    global p
    tmp=n//3
    if tmp==0:
        return
    for i in range(x+n//3,x+n//3*2):
        for j in range(y+n//3,y+n//3*2):
            p[i][j]=" "
    for i in range(0,n,tmp):
        for j in range(0,n,tmp):
            three(x+i,y+j,tmp)

p = [["*" for i in range(n)] for i in range(n)]

if n==3:
    p[n//3][n//3]=" "
else:
    three(0,0,n)
            
for i in range(n):
    for j in range(n):
        print(p[i][j],end='')
    print()
