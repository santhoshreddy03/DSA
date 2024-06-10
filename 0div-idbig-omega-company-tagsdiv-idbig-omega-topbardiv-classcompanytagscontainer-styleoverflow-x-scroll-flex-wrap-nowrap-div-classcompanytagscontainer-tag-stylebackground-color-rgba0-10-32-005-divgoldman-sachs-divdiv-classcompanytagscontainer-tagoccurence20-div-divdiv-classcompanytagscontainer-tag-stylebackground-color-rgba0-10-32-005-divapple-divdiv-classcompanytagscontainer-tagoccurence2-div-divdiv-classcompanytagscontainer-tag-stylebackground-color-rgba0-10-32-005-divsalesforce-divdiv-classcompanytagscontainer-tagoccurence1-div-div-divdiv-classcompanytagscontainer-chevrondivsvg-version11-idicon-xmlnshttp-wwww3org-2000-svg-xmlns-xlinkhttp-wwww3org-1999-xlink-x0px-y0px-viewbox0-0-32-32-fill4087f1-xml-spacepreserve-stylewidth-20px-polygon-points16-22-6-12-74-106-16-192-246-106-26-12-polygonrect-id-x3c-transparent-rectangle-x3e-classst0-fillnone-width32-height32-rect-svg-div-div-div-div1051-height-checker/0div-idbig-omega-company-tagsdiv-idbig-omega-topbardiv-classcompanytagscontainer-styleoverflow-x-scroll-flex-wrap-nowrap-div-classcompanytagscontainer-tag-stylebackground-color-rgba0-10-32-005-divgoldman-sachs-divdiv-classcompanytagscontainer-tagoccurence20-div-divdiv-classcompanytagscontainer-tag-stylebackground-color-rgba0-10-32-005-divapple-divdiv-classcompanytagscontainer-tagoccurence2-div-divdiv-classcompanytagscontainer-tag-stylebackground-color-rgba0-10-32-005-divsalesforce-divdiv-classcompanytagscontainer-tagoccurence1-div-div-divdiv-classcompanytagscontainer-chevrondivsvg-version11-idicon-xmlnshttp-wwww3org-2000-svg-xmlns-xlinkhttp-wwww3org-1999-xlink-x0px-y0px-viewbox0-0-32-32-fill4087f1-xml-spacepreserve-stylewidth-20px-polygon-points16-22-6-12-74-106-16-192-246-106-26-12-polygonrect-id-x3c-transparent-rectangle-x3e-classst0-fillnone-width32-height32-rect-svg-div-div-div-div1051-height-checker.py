class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        real=[]
        c=0
        for i in heights:
            real.append(i)
        heights.sort()
        for i in range(len(real)):
            if real[i]!=heights[i]:
                c+=1
        return c
                