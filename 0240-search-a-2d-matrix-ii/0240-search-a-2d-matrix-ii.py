class Solution(object):
    def searchMatrix(self, matrix, target):
        def bs(a,n,target):
            low,high=0,n-1
            while low<=high:
                mid=(low+high)//2
                if a[mid]==target:
                    return True
                if a[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return False
        ans=False
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                ans=bs(matrix[i],len(matrix[i]),target)
                if ans:
                    return ans
        return ans
        