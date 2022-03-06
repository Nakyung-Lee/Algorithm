def solution(answers):
    answer=[]
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    a=0
    b=0
    c=0
    tot=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==p1[a]:
            tot[0]+=1
        if answers[i]==p2[b]:
            tot[1]+=1
        if answers[i]==p3[c]:
            tot[2]+=1
        a+=1
        b+=1
        c+=1
        if a==5:
            a=0
        if b==8:
            b=0
        if c==10:
            c=0
    k=max(tot[0],tot[1],tot[2])
    if k==tot[0]:
        answer.append(1)
    if k==tot[1]:
        answer.append(2)
    if k==tot[2]:
        answer.append(3)
    return answer
