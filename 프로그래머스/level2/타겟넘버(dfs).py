numbers=[1,1,1,1,1]
target=3


def dfs(i,numbers,value,target):
    answer = 0
    if (i==len(numbers) and value==target):             
        return 1
    if (i==len(numbers)):
        return 0
    answer+=dfs(i+1,numbers,value+numbers[i],target)
    answer+=dfs(i+1,numbers,value-numbers[i],target)
    return answer
    
def solution(numbers,target): 
    answer=dfs(0,numbers,0,target)
    return answer


print(solution(numbers,target))
