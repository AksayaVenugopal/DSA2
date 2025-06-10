class Solution:
    def fib(self, n: int) -> int:
        
        if n<=1:
            return n
        def f(w):
            if w<=1:
                return w
            n1=f(w-1)
            n2=f(w-2)
            n3=(n1+n2)
            return n1+n2
        c=f(n)
        return c
        