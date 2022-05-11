N=int(input())

s = list(map(int,input().split()))

#오름차순 정렬
s=sorted(s) 

result=0
cnt=0

#공포도 낮은 것부터 하나씩 확인 
for i in s:
    #모험가 수 
    cnt += 1
    #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상 => 그룹 결성
    if cnt>=i:
        #그룹 수
        result+=1
        cnt=0

print(result)


