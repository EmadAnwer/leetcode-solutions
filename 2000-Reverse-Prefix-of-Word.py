class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        try:
            i = word.index(ch) + 1
            return word[:i][:: -1] + word[i:]
        except:
            return word