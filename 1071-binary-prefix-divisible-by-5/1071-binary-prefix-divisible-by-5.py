class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=0
        w=[]
        for i in range(len(nums)):
            res=res | nums[i]
            if res%5==0:
                w.append(True)
            else:
                w.append(False)
            res=res<<1
        return w
        