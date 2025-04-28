class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(opened,closed):
            if opened==closed==n:
                res.append("".join(stack))
            if opened<n:
                stack.append("(")
                backtrack(opened+1,closed)
                stack.pop()
            if opened>closed:
                stack.append(")")
                backtrack(opened,closed+1)
                stack.pop()
        w=backtrack(0,0)
        return res