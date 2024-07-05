
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score) # em
        scores_map = {}
        for i, s in enumerate(score):
            scores_map[s] = i
        
        for i in range(len(sorted_score) - 3):
            idx = scores_map[sorted_score[i]]
            score[idx] = str(len(sorted_score) - i)
        
        
        ms = ["Gold Medal","Silver Medal", "Bronze Medal"]
        

        for i ,m in enumerate(ms):
            if i + 1 <= len(score):                
                idx = scores_map[sorted_score[(i + 1) * -1]]
                score[idx] = m

        return score