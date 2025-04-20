class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        mini=nums[low]
        while low<high:
            mid=(low+high)//2
            if nums[mid]<nums[mid]:
                high=mid
            elif nums[mid]>nums[high]:
                low=mid+1
            else:
                high-=1
        return nums[low]
        