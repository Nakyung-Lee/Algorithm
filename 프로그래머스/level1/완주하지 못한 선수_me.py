'''
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
-> 불일치하는 하나의 경우 나오면 바로 끝내도 된다,, 조건 주의하기
'''
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i not in completion:
            answer=i
        else:
            completion.remove(i)
    return answer
  
'''
remove() 는 처음부터 탐색하는 아주 비효율적인 함수
-> 비록 for문을 하나 썼지만 remove 로 인해서 O(n^2) 의 시간복잡도를 갖게되어 효율성 부분 -> 0점 / 정확성 100
'''

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    if len(answer)==0:
        return participant[-1]    
    return answer
  
'''
정렬 먼저 하고 시작
같지 않은 값이 있으면 바로 return 끝
전부 다 돌아도 값이 없을 경우에는 마지막 주자가 완주하지 못한 선수.
'''
