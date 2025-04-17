class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def nh(piles,n):
            g=0
            
            for i in range(len(piles)):
                r=piles[i]%n
                q=piles[i]//n
                if r!=0:
                    g+=1+q
                else:
                    g+=q
            
            return g
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            hours=nh(piles,mid)
            if hours>h:
                low=mid+1
            else:
                high=mid-1
        return low
                