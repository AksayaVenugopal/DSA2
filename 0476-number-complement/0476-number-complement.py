class Solution:
    def findComplement(self, num: int) -> int:
        w=num.bit_length()
        w=(1<<w)-1
        return num ^ w