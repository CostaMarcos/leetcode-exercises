class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ms = "@"
        for c in s:
            ms += "#" + c
        ms += "#$"

        n = len(ms)
        left = right = 0
        p = [0] * n
        longest = 0
        position = 0

        for i in range(1, n -1):
            mirror = left + right - i

            if i < right:
                p[i] = min(right - i, p[mirror])
            
            while ms[i + 1 + p[i]] == ms[i-1-p[i]]:
                p[i] += 1

                if p[i] > longest:
                    longest = p[i]
                    position = i

            if i + p[i] > right:
                left = i - p[i]
                right = i + p[i]

        start = position-longest+1
        end = 0
        result = ''
        while end != longest:
            if not ms[start] in ["#", "@", "$"]:
                result += ms[start]
                end += 1
            
            start += 1
        return result


a = Solution()
print(a.longestPalindrome('babad'))
print(a.longestPalindrome('arara'))