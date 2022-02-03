#내 풀이 
'''
def solution(n):
    answer=''
    if n<4:
        if n==3:
            answer='4'
        else:
            answer+=str(n)
    while n>3:     
        if n%3==0:
            answer='4'+answer
            n=n//3 - 1
        else:
            answer=str(n%3)+answer
            n=n//3
        if n < 4 and n !=0:
            answer=str(n)+answer
    answer=answer.replace('3','4')
    return answer
'''

# best 풀이
def solution(n):
    num = ['1','2','4']
    answer = ""

    '''
    값을 계속해서 앞부분에 저장하기 위해서 
    answer = 값 + answer
    '''
    
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
n=int(input())
print(solution(n))
