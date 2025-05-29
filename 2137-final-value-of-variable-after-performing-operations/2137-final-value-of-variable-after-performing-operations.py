class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a=["++X","X++"]
        x=0
        for i in operations:
            if i in a:
                x+=1
            else:
                x-=1
        return x