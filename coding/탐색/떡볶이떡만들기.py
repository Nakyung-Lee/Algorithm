#떡의 개수 (n) 요청한 떡의 길이 (m)
n,m = list(map(int,input().split(' ')))
#각 떡의 개별 높이 정보 입력
arr = list(map(int,input().split()))

#이진 탐색 위한 시작점, 끝점
start = 0
end = max(arr)

#이진탐색 수행(반복적)
result = 0
while(start<=end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
           
           
