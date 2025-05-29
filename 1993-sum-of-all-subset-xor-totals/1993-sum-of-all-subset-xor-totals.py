class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        w=[]
        for i in range(2**len(nums)):
            t=[]
            for j in range(len(nums)):
                if i&(1<<j):
                    t.append(nums[j])

            x=0
            for k in range(len(t)):
                x=x^t[k]
            w.append(x)
        return sum(w)


        