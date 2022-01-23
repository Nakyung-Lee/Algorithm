array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  #인덱스 i부터 1까지 감소하며 반복
    for j in range(i,0,-1):
      #한칸씩 왼쪽으로 이동
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
      #자기보다 작은 값 만나면 멈춤
        else:
            break

print(array)

'''
삽입 정렬 시간 복잡도 O(N^2)
현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
최선의 경우 시간 복잡도 O(N) 
'''
