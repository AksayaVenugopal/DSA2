class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r=[1,1]
        if rowIndex==0:
            return [1]
        for i in range(1,rowIndex):
            w=r
            r=[1]
            k=1
            for j in range(0,i):
                a=w[j]+w[j+1]
                r.append(a)
            r.append(1)
        return r


        