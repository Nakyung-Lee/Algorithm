def solution(N, stages):
    result = {}
    l = len(stages)
    for stage in range(1, N+1):
        if l != 0:
            # count 함수 사용
            count = stages.count(stage)
            result[stage] = count / l
            l -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
  
'''
result는 dictionary
sorted에 result를 그냥 넘기면 result의 keys가 들어간다
keys는 생략 가능
lambda 기준 result[x]: -> value로 정렬한다는 뜻
따라서 key 출력된다
'''

'''
람다(lambda) 함수
- 두 수를 더하는 함수
def hap(x,y):
return x+y
-> (lambda x,y:x+y)(10,20)

'''
