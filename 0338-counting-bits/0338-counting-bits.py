class Solution:
    def countBits(self, n: int) -> List[int]:
        def bitt(n):
            c=0
            while n!=0:
                c+=1
                n=n&n-1
            return c
        w=[]
        for i in range(n+1):
            w.append(bitt(i))
        return w
            
        