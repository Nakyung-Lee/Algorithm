import sys
import heapq

N=int(input())

s=[list(map(int,input().split())) for _ in range(N)]

s.sort()


room=[]

heapq.heappush(room,s[0][1])

for i in range(1,N):
    if room[0] <= s[i][0]:
        heapq.heappop(room)
        heapq.heappush(room,s[i][1])
    else:
        heapq.heappush(room,s[i][1])

print(len(room))
