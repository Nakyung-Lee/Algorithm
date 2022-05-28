from bisect import bisect_left, bisect_right

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index


n,x = list(map(int,input().split()))

arr = list(map(int,input().split()))

#값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(arr,x,x)

if count == 0:
    print(-1)
else:
    print(count)

