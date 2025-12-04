class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1:
            return s

        r = [''] * numRows
        pos = 1
        way_positive = True

        while s != '':
            r[pos-1] = r[pos-1] + s[0]

            s = s[1:]

            if way_positive:
                if pos == numRows:
                    pos -= 1
                    way_positive = not way_positive
                else:
                    pos += 1
            else:
                if pos == 1:
                    pos += 1
                    way_positive = not way_positive
                else:
                    pos -= 1
            
        return ''.join(r)


a = Solution()
print(a.convert("PAYPAALISHIRING", 4))