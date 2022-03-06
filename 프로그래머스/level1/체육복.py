n=5
lost=[2,4]	
reserve=[1,3,5]

def solution(n, lost, reserve):
    answer = 0
    num=[]
    for i in range(1,n+1):
        num.append(1)
    for j in range(len(lost)):
        num[lost[j]-1]-=1
    for l in range(len(reserve)):
        num[reserve[l]-1]+=1
    for k in range(n):
        if num[k]==2:
            if k==0 or k==n-1:
                if k==n-1:
                    if num[k-1]<1:
                        num[k-1]+=1
                        num[k]-=1
                if k==0:
                    if num[k+1]<1:
                        num[k+1]+=1
                        num[k]-=1
            else:
                if num[k-1]<1:
                    num[k-1]+=1
                    num[k]-=1
                elif num[k+1]<1:
                    num[k+1]+=1
                    num[k]-=1
    for m in range(len(num)):
        if num[m]>=1:
            answer+=1
    return answer

print(solution(n,lost,reserve))
