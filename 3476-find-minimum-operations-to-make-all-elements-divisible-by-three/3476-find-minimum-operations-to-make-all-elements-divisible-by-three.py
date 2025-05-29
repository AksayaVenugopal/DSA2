class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if i%3==2:
                s+=1
            else:
                s+=(i%3)

        return s
        