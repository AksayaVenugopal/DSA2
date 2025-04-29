class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        s=[]
        for i in range(len(image)):
            s1=[]
            for j in range(len(image)-1,-1,-1):
                s1.append(image[i][j]^1)
            s.append(s1)
        return s



        