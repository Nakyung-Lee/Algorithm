def solution(priorities, location):
   
    value = priorities
    idx = [id for id in range(len(priorities))]
    
    i = 0
    while True:
        if value[i] < max(value[i+1:]):
            value.append(value.pop(i))
            idx.append(idx.pop(i))
        else :
            i+=1
        
        if value ==sorted(value,reverse=True):
            break
    return idx.index(location)+1

priorities = [1, 2, 3, 8,1]
location = 0
print(solution(priorities,location))
