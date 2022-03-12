n=int(input())
score=[]

for i in range(n):
    score.append(input().split())

'''
1, ko가 감소하는 순서로 정렬
2. 1이 같으면 en이 증가하는 순서로 정렬
3. 2가 같으면 ma가 감소하는 순서로 정렬
4. 3이 같으면 이름 사전 순으로 증가하는 순서로 정렬
'''

score.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))


for i in range(n):
    print(score[i][0])
