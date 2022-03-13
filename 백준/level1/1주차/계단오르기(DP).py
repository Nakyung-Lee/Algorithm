n=int(input())

step=[]
#시작
step.append(0)

for i in range(n):
    x=int(input())
    step.append(x)

#계단이 하나라면
if n==1:
    print(step[1])
else:
    d=[0]*(n+1)
    d[1]=(max(d[0]+step[1],step[1]))
    d[2]=(max(d[0]+step[2],d[1]+step[2]))
    '''
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
    '''
    for i in range(3,n+1):
        d[i]=(max(d[i-2]+step[i],d[i-3]+step[i-1]+step[i]))
        
    print(d[n])
