s="aabbaccc"

def solution(s):
    answer = len(s)
    '''
    최대 절반의 길이까지
    슬라이싱 주의 s[:len(s)//2 + 1] 이 절반
    '''
    for n in range(1,len(s)//2 + 2):
        tot=""
        #하나씩은 존재 하니까
        cnt=1
        #tmp에 슬라이싱 해서 저장
        tmp=s[:n]
        '''
        n개의 크기만큼 건너뛰면서 문자열 확인
        len(s)+n 남는 문자들 저장하기 위해
        '''
        for i in range(n,len(s)+n,n):
            if tmp==s[i:i+n]:
                cnt+=1
            else:
                #cnt==1이라면 문자 저장
                if cnt==1:
                    tot+=tmp
                #cnt 문자로 바꿔 저장 
                else:
                    tot+=(str)(cnt)+tmp
                cnt=1
                #tmp
                tmp=s[i:i+n]
        answer=min(len(tot),answer)
    return answer

print(solution(s))
