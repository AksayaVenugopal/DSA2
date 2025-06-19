class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def f(ind,arr,ans,ds):
            ans.append(ds[:])    
            for i in range(ind,len(arr)):
                if i!=ind and arr[i]==arr[i-1]:
                    continue
                ds.append(arr[i])
                f(i+1,arr,ans,ds)
                ds.pop()
        ans,ds=[],[]
        f(0,nums,ans,ds)
        return ans
        
        