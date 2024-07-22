class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_map = {}
        for name, hight in zip(names, heights):
            people_map[hight] = name

        heights.sort(reverse=True)

        for i ,h in enumerate(heights):
            
            names[i] = people_map[h]
        
        return names