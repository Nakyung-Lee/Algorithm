'''
6마리의 폰켓몬 -> 3마리의 폰켓몬을 골라야 한다
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리, 2번 폰켓몬 한 마리, 4번 폰켓몬 한 마리
-> 3 

문제만 읽었을 때는 어렵게 느껴졌는데,, 왠걸? 푸니까 겁나 쉬운거네,, 우쒸
'''

nums=[3,3,3,2,2,4]

def solution(nums):
    answer = 0
    a=len(nums)//2
    nums=set(nums)
    for i in range (len(nums)):
        if answer<a:
            answer+=1
    return answer
 
print(solution(nums))
