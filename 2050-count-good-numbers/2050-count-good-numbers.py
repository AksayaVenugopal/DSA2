class Solution:
    def countGoodNumbers(self, n: int) -> int:
        o=[2,3,5,7]
        e=[0,2,4,6,8]
        r=n%2
        q=n//2
        m=(10**9)+7
        w=pow(4,q,m)*pow(5,(q+r),m)
        return w%m
        