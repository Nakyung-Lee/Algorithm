scoville = [2, 12, 10 , 9, 1, 3]
K = 7

import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0]<K:
        min1,min2=heapq.heappop(scoville),heapq.heappop(scoville)
        tmp=min1+min2*2
        if len(scoville)==1 and scoville[0]<K:
            return -1
        heapq.heappush(scoville,tmp)
        answer+=1
        print(scoville)
    return answer

print(solution(scoville, K))
