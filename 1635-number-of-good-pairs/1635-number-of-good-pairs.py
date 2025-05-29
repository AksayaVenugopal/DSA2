import math


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        s=0
        print(d)
        for j in d:
            if d[j]>1:
                s+=(d[j]*(d[j]-1))/2
        return int(s)

        