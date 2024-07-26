class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dict={"U":0,"D":0, "L":0, "R":0}
        
        for i in moves:
            if i in dict:
                dict[i]+=1
        return dict["U"]==dict["D"] and dict["R"]==dict["L"]