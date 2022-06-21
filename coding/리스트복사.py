import copy

s=[[0,1,2,3,4]]

tmp=copy.deepcopy(s)
tmp[0][0]=-1
print(tmp[0][0],s[0][0])
