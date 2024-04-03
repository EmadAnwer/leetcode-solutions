from collections import defaultdict, deque
from typing import List


# class Solution:
#     def is_the_same_word(self, s1: str, s2: str):
#         if len(s1) != len(s2):
#             return False
#         return "".join(sorted(s1)) == "".join(sorted(s2))

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         output: list = []
#         list_bool = [False] * len(strs)
#         for i in range(len(strs)):
#             if list_bool[i] == False:
#                 new_list = []
#                 new_list.append(strs[i])
#                 list_bool[i] = True

#                 for j in range(i, len(strs)):
#                     if not list_bool[j]:
#                         if self.is_the_same_word(strs[i], strs[j]):
#                             new_list.append(strs[j])
#                             list_bool[j] = True

#                 output.append(new_list)
#         return output


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(word)

        return list(res.values())


strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
s = Solution()
out = s.groupAnagrams(strs)


print(f"output :{out}")
