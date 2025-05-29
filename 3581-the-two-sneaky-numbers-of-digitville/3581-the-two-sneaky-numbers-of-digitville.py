class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        w=list(set(nums))
        s=[]
        for i in range(len(w)):
            nums.remove(w[i])
        return nums        