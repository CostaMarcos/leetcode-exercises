class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        r = [[1]] * numRows

        for idx, v in enumerate(r):

            if idx == 0:
                continue

            current = [1]*(idx+1)
            
            if idx == 1:
                r[idx] = current
                continue

            for idx2 in range(1, idx):
                current[idx2] = r[idx-1][idx2-1] + r[idx-1][idx2]
            
            r[idx] = current

        return r


a = Solution()
a.generate(4)
