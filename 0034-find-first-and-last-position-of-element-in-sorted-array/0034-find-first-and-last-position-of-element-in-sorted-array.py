class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        n=len(nums)
        mid=low+(high-low)//2
        start=-1
        end=-1
        while low<=high:
            
            if nums[mid]==target:
                if n==1:
                    return [0,0]
            
                start=mid
                end=mid
                print(start,end)
                while end<n-1:
                    if nums[end+1]==target:
                        end+=1
                    else:
                        break
                while 1<=start:
                    if nums[start-1]==target:
                        start-=1
                    else:
                        return [start,end]
                return [start,end] 
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
            mid=low+(high-low)//2
            
        return [start,end]

        