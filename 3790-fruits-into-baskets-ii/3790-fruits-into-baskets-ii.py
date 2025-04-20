class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=len(fruits) 
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    print(fruits[i],baskets[j])
                    c-=1
                    baskets.pop(j)

                    break
        return c