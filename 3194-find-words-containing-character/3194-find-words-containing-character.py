class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        s=[]
        for i in range(len(words)):
            cw=words[i]
            for j in range(len(cw)):
                if cw[j]==x:
                    s.append(i)
                    break
        return s
        