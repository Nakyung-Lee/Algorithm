N=int(input())

s = list(input().split())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
x,y=1,1

for i in range(len(s)):
    if s[i]=='R':
        if x + dx[0] <= N and x + dx[0] > 0 and y + dx[0] <= N and y + dx[0] > 0:
            x+=dx[0]
            y+=dy[0]        
    elif s[i]=='U':
        if x + dx[1] <= N and x + dx[1] > 0 and y + dx[1] <= N and y + dx[1] > 0:
            x+=dx[1]
            y+=dy[1] 
    elif s[i]=='L':
        if x + dx[2] <= N and x + dx[2] > 0 and y + dx[2] <= N and y + dx[2] > 0:
            x+=dx[2]
            y+=dy[2] 
    elif s[i]=='D':
        if x + dx[3] <= N and x + dx[3] > 0 and y + dx[3] <= N and y + dx[3] > 0:
            x+=dx[3]
            y+=dy[3]
print(x,y)

-------------------------------------------------------------------------------------

N = int(input())

s = input().split()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_types=['R','U','L','D']

x,y=1,1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    # 공간을 벗어나는 경우에는 x,y 업데이트 시켜주지 않는다. 
    x,y=nx,ny
    
print(x,y)
