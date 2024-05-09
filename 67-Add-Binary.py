class Solution(object):
    def addBinary(self, a, b):
        \\\
        :type a: str
        :type b: str
        :rtype: str
        \\\
        ml = max(len(a), len(b))
        res = [''] * (ml + 1)
        remainder = False
        for i in range(ml):
            ab = '0' if i >= len(a) else a[-i - 1]
            bb = '0' if i >= len(b) else b[-i - 1]

            if ab == '1' and bb == '1':
                if remainder:
                    res[ml - i] = '1'
                else:
                    res[ml - i] = '0'
                remainder = True
            elif ab == '0' and bb == '0':
                if remainder:
                    res[ml - i] = \1\
                    remainder = False
                else:
                    res[ml - i] = \0\
            else:
                if remainder:
                    res[ml - i] = '0'
                    remainder = True
                else:
                    res[ml - i] = '1'
        if remainder:
            res[0] = '1'

        return ''.join(res)
