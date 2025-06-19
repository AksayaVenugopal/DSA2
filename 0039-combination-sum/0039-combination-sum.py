class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(ind,target,arr,ans,ds):
            if (ind==len(arr)):
                if target==0:
                    ans.append(ds[:])
                return
            if arr[ind]<=target:
                ds.append(arr[ind])
                f(ind,target-arr[ind],arr,ans,ds)
                ds.pop()
            f(ind+1,target,arr,ans,ds)
        ans,ds=[],[]
        f(0,target,candidates,ans,ds)
        return ans
