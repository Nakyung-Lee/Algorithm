a,b=map(int,input().split())
day=["MON","TUE", "WED", "THU", "FRI", "SAT","SUN"]
j=0
for i in range(1,a):
    if i==2:
        j+=28
    elif i==4 or i==6 or i==9 or i==11:
        j+=30
    else:
        j+=31
j+=b

j=j-1
print(day[(j%7)])
