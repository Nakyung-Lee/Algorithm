from itertools import product
import collections

S1, S2, S3 = map(str, input().split())

s1 = range(1,int(S1)+1)
s2 = range(1,int(S2)+1)
s3 = range(1,int(S3)+1)

items = [s1,s2,s3]

result = []

for i in list(product(*items)):
    result.append(sum(i))

counter = collections.Counter(result)
print(sorted(counter,key=lambda x : counter[x], reverse = True)[0])

'''
result = [i + j + m for i in range(1, int(s1)+1) for j in range(1, int(s2)+1) for m in range(1, int(s3)+1)]

print(collections.Counter(result).most_common(1)[0][0])
'''