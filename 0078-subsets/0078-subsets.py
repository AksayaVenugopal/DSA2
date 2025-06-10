class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
 #       n=len(nums)
  #      o=[]
   #     for i in range((2**n)):
    #        temp=[]
     #       for j in range(n):
      #          if i&(1<<j):
       #             temp.append(nums[j])
        #    o.append(temp)
       # return o




        a=[]
        
        def f(ind,arr,nums,a):
            
            if ind>=len(nums):
                print(arr)
                a.append(arr[:])
                return
            arr.append(nums[ind])
            f(ind+1,arr,nums,a)
            arr.remove(nums[ind])
            f(ind+1,arr,nums,a)
        s=[]
        f(0,s,nums,a)
        return a