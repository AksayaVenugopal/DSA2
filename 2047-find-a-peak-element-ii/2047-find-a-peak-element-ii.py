class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        w=[-1]*(len(mat)+2)
        mat.insert(0,w)
        mat.insert(len(mat),w)
        for i in range(len(mat)):
            mat[i].insert(0,-1)
            mat[i].insert(len(mat[i]),-1)
        
        for i in range(1,len(mat)-1):
            for j in range(1,len(mat[i])-1):
                print(i,j)
                up=mat[i-1][j]
                down=mat[i+1][j]
                right=mat[i][j+1]
                left=mat[i][j-1]
                if mat[i][j]>up and mat[i][j]>down and mat[i][j]>right and mat[i][j]>left:
                    return [i-1,j-1]

        
        