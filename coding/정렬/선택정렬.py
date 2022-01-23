array=[7,5,9,0,3,1,6,2,4,8]

'''
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]
'''

'''
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
            tmp=array[j]
            array[j]=array[i]
            array[i]=tmp
'''

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
          #swap : 특정 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
            array[i],array[j]=array[j],array[i] 
            
print(array)
