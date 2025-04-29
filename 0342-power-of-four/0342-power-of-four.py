class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n==1:
            return True
        if n<=0 or n<4:
            return False
        r=math.log(n,4)
        if (r/int(r))==1:
            return True
        return False
        