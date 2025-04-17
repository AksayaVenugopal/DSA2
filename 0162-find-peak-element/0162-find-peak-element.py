class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        j=-2
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            if nums[0]>nums[1]:
                return 0
            elif nums[1]>nums[0]:
                return 1
        if nums[n-1]>nums[n-2]:
            return n-1
            
        for i in range(0,len(nums)-2):
            if i==0 :
                if nums[i]>nums[1]:
                    return 0
        
            if nums[i]>nums[i-1] and nums[i]>nums[i+1] :
                return i
            elif nums[j]>nums[j-1] and nums[j]>nums[j+1]:
                return n+j
            j=j-1
        if nums[n-1]>nums[n-2]:
            return n-1
        return -1
        