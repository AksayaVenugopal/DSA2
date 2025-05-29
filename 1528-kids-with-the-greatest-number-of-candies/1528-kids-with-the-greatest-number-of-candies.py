class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        e=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                e.append(True)
            else:
                e.append(False)
        return e

        