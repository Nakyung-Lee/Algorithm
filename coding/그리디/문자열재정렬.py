data=input()

st=[]
num=[]

for i in range(len(data)):
    if data[i]>='A' and data[i]<='Z':
        st.append(data[i])
    else:
        num.append(int(data[i]))
        
st.sort()
s=sum(num)

for i in range(len(st)):
    print(st[i],end='')
    
print(s,end='')

-------------------------------------------------------------

data=input()

result=[]
value=0

for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value+=int(x)

result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

#최종 결과 출력 (리스트 -> 문자열)
print(''.join(result))
