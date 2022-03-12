import sys

n=int(input())

#메모리 초과 오류 해결

'''
**계수 정렬(Counting Sort) 알고리즘**
배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
데이터가 등장한 횟수를 셈

예시)
3이 2번 등장 : 3의 인덱스는 2
7이 1번 등장 : 7의 인덱스는 1
→ 앞에서부터 진행해서 수 하나씩 등장할 때마다 인덱스를 하나씩 증가

'''

nums=[0]*10001

for i in range(n):
    num=int(sys.stdin.readline())
    nums[num]+=1


for i in range(10001):
    if nums[i]!=0:
        for j in range(nums[i]):
            print(i)

