'''
딕셔너리 (내 풀이)
def solution(participant, completion):
    dic = {}
    for part in participant:
        dic[part] = 0
    for part in participant:
        dic[part] += 1
    for com in completion:
        if com in dic.keys():
            dic[com]-=1
    for d in dic:
        if dic[d]>=1:
            return d
'''

'''
** 해시 구조 **
키(Key)와 값(Value)쌍으로 이루어진 데이터 구조
Key를 이용하여 데이터를 찾으므로, 속도를 빠르다
파이썬 -> 딕셔너리(Dictionary) 타입이 해쉬 테이블과 같은 구조

시간 복잡도
일반적인 경우(충돌이 없는 경우): O(1)
최악의 경우(모든 경우에 충돌이 발생하는 경우): O(n)

'''
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
 
'''
zip 복수개의 iterable 객체로부터 같은 idx의 원소들을 비교할 때 사용
'''
 def solution(participant, completion):
   answer = ''
   participant.sort()
   completion.sort()
   for p,c in zip(participant, completion): 
       if p != c:
           return p 
   return participant.pop()

'''
데이터의 개수를 셀 때 유용한 파이썬의 collections 모듈의 Counter 클래스 
데이터 개수 셀 때 파이썬 내장 자료구조인 딕셔너리 사용

파이썬에서 제공하는 collections 모듈의 Counter 클래스 사용예시
from collections import Counter

Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

'''
결과는 dictionary 형태로 나오고 list(answer.keys())[0] 
 -> answer로 부터 Keys를 꺼내온다
Keys를 list로 형변환 하고 이 중 0번 째 인덱스의 값을 읽어온다
'''
