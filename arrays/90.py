class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, j = 0,0

        while j < len(nums) or i < len(nums):

            actual = nums[i:j]

            if actual not in result:
                result.append(actual)

            if j <= len(nums):
                j += 1
            else:
                i += 1

        return result

a = Solution()
print(a.subsetsWithDup([1, 2, 3]))