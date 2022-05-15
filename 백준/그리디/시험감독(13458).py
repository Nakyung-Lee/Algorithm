import sys
import math

N=int(input())

num=list(map(int,sys.stdin.readline().split()))

b,c = map(int,sys.stdin.readline().split())


#총 감독관 1명씩 (시험장 수만큼)
cnt=N

for x in num:
    #총 응시자 수 - 총 감독관 수 
    x=x-b
    #남은 응시자들 있으면
    if x>0:
        #응시자 남은 수에서 부 감독관 수 나누기
        cnt+=math.ceil(x/c)

print(cnt)
