class Solution(object):
    def splitArray(self, nums, k):
        def f(tar,nums):
            s=0
            ss=1
            for i in range(len(nums)):
                s+=nums[i]
                if s>tar:
                    s=nums[i]
                    ss+=1
            print(tar,ss)
            return ss
                
                

        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if f(mid,nums)>k:
                low=mid+1
            else:
                high=mid-1
        return low
        
        