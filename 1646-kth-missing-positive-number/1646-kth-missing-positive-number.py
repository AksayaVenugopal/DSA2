class Solution(object):
    def findKthPositive(self, arr, k):
        
        kk=0
        def bs(tar,arr):
            low,high=0,len(arr)-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==tar:
                    return True
                if arr[mid]>tar:
                    high=mid-1
                else:
                    low=mid+1
            return False

        last=0
        for i in range(1,arr[-1]+1):
            if kk==k:
                return last
            if not bs(i,arr):
                last=i
                kk+=1
        if last==0 or kk<k:
            return arr[-1]+k-kk



        