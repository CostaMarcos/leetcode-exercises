class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        current = None
        vl = 1

        for pos in nums:

            if current is None:
                current = pos
                vl = 1
                continue

            if pos == current:
                vl += 1

            if pos != current and vl > 1:
                current = pos
                vl = 1
            
            if pos != current and vl == 1:
                return current
        
        return current


a = Solution()
a.singleNumber([1,0,1])