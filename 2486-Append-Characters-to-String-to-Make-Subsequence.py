class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr = 0  
        t_ptr = 0
        chars_to_append = 0
        
        while t_ptr < len(t) and s_ptr < len(s):
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1

        chars_to_append = len(t) - t_ptr
        
        return chars_to_append
