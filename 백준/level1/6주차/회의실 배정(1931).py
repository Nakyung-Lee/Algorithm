import sys

N=int(input())

s=[[0]*2 for _ in range(N)]

for i in range(N):
    t1,t2=map(int,sys.stdin.readline().split())
    s[i][0]=t1
    s[i][1]=t2

#시작시간 오름차순으로 정렬 -> 끝나는 시간으로 오름차순 정렬
'''
4
0 10
3 4
2 3
1 2
-> 입력 순서대로라면 0 10 으로 1번의 회의 가능,
-> 끝나는 시간으로 정렬, (1 2) (2 3) (3 4) (4 10) 총 4번 가능

2
2 2
1 2
-> 끝나는 시간이 같다면 빨리 시작하는 순서대로 정렬 되어야 한다.
'''

s.sort(key=lambda x:(x[1],x[0]))

cnt=1

a=s[0][0]
b=s[0][1]

#print(s)

for i in range(1,N):
    if s[i][0]>=b:
        cnt+=1
        b=s[i][1]
print(cnt)
