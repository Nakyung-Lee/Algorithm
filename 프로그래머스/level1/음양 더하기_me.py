absolutes=[4,7,12]
signs=[True,False,True]

def solution(absolutes,signs):
    answer=123456789
    for i, value in enumerate(absolutes):
        if signs[i]==False:
            absolutes[i]=0-value
    answer=sum(absolutes)
    return answer

print(solution(absolutes,signs))
