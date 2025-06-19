class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(ind,target,arr,ans,ds):
            if target<0:
                return
            elif target==0:
                ans.append(ds[:])
            else:    
                for i in range(ind,len(arr)):
                    if i>ind and arr[i]==arr[i-1]:
                        continue
                    if arr[i]>target:
                        break
                    ds.append(arr[i])
                    f(i+1,target-arr[i],arr,ans,ds)
                    ds.pop()
        ans,ds=[],[]
        candidates.sort()
        f(0,target,candidates,ans,ds)
        return ans
            

        