data=input()

row=int(data[1])
col=int(ord(data[0]))-int(ord('a')) +1

print(row,col)

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2)]

#8가지 방향에 대하여 각 위치로 이동 가능한지 확인

result=0
for step in steps:
    #이동하고자 하는 위치 확인
    n_row = row + step[0]
    n_col = col + step[1]
    if n_row>=1 and n_row<=8 and n_col>=1 and n_col<=8:
        print(n_row,n_col)
        result+=1

print(result)
