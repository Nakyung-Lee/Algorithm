progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]	

import math
def solution(progresses,speeds):
    answer=[]
    day={}
    max_day=0
    for p,s in zip(progresses,speeds):
        time=math.ceil((100-p)/s)
        if max_day<time:
            max_day=time
            day[max_day]=[max_day]
        else:
            day[max_day].append(time)
    print("day : ", day) 
    #day :  {5: [5], 10: [10, 1, 1], 20: [20, 1]}
    print("day.values : ",day.values())
    #day.values :  dict_values([[5], [10, 1, 1], [20, 1]])
    print("day.keys : ",day.keys())
    #dict_keys([5, 10, 20])
    answer=[len(v) for v in day.values()]
    return answer
    

print(solution(progresses,speeds))
