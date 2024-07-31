class Solution:
    def reverseWords(self, s: str) -> str:
        words: list[str] = s.split()

        reversed_words = [word[::-1] for word in words]

        return " ".join(reversed_words)