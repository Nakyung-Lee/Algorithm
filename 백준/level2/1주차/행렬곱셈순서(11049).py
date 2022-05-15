import sys
sys.setrecursionlimit(10000)

def func(x,y):
    #이미 dp 구한거다
    if dp[x][y]!=0:
        return dp[x][y]
      
    #행렬 2개는 있어야 곱셈 한다. -> 곱셈 불가능
    if y==x:
        return 0
      
    #max값
    r=float('inf')
    for k in range(x,y):
        mm=min(r,func(x,k)+func(k+1,y)+R[x]*C[k]*C[y])
        r=mm
    dp[x][y]=r
    return r

N=int(sys.stdin.readline())
R=[]
C=[]
dp=[[0]*N for i in range(N)]
for i in range(N):
    r,c=map(int,sys.stdin.readline().split())
    R.append(r)
    C.append(c)

#인접한 배열 미리 곱해서 배열에 넣고
for i in range(N-1):
    dp[i][i+1]=R[i]*R[i+1]*C[i+1]
    
print(func(0,N-1))
