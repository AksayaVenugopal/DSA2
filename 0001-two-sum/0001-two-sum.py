class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(nums)):
            t=nums[i]
            l=nums[i+1:]
            minus=target-t
                
            if minus in l:
                    output.append(i)
                    output.append(l.index(minus)+i+1)
                    break

        return output