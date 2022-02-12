N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    answer = []
    an=[]
    dic={}
    l=len(stages)
    for j in range(1,N+1):
        cnt=0
        for i in range(0,len(stages)):
            if j-1<stages[i] and stages[i]<=j:
                cnt+=1
        print(cnt,l,cnt/l)
        answer.append(cnt/l)
        dic[j]=answer[j-1]
        l=l-cnt
        if l==0:
            l=1
    dict= sorted(dic.values(), reverse=True)
    for i in range(len(dict)):
        for key,value in dic.items():
            if dict[i]==value:
                print('key : ', key)
                an.append(key)
                dic[key]='0'
    return an

'''
N=5
stages=[2,2,2,2,2]
0으로 나누게 될때 런타임 에러 오류

해결 -> if l==0:    l=1
'''
