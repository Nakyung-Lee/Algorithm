N = int(input())

dic={}
for _ in range(N):
    n = input()
    dic[n]=len(n)

#길이가 짧은 것부터
dic = dict(sorted(dic.items(), key=lambda x : x[0]))

#길이가 같으면 사전 순으로
dic = sorted(dic.items(), key=lambda x : x[1])


for i in range(len(dic)):
    print(dic[i][0])
