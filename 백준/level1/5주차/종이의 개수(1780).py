import sys
a1=0
a2=0
a3=0
def devide(x, y, n):
    global a1,a2,a3
    num = p[x][y] 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != p[i][j]:
                # 1, 2, 3
                devide(x, y, n // 3)
                devide(x, y + n // 3, n // 3)
                devide(x, y + n // 3 * 2, n // 3)
                # 4, 5, 6
                devide(x + n // 3, y, n // 3)              
                devide(x + n // 3, y + n // 3, n // 3)
                devide(x + n // 3, y + n // 3 * 2, n // 3)
                # 7, 8, 9
                devide(x + n // 3 * 2, y, n // 3)
                devide(x + n // 3 * 2, y + n // 3, n // 3)
                devide(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
            
    if num == -1:
        a1 += 1
    elif num == 0:
        a2 += 1
    elif num == 1:
        a3 += 1
n=int(input())

p=[]

for i in range(n):
    p.append(list(map(int, sys.stdin.readline().split())))


devide(0,0,n)

print(a1)
print(a2)
print(a3)


