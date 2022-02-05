nums=[1,2,7,6,4]

def solution(nums):
    cnt=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                a=0
                tot=nums[i]+nums[j]+nums[k]
                for l in range(2,tot):
                    if tot%l==0:
                        a+=1
                if a==0:
                    cnt+=1
    return cnt

print(solution(nums))
