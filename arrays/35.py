# Search Insert Position
# https://leetcode.com/problems/search-insert-position


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] > target:
            return 0
        elif len(nums) == 1 and nums[0] < target:
            return 1


        while left < right:

            i_left = nums[left]
            i_right = nums[right]

            if nums[left] == target:
                return left
            elif i_left < target:
                left += 1
            elif i_left > target:
                left = 0 if left <= 1 else left - 1

            if i_right == target:
                return right
            elif i_right > target:
                right -= 1
            elif i_right < target:
                return right + 1
        
        return left
            



tests = Solution()

test1 = [1,3,5,6]
_input1 = 5
result1 = 2

test2 = [1,3,5,6]
_input2 = 2
result2 = 1

test3 = [1,3,5,6]
_input3 = 7
result3 = 4

test4 = [1, 4, 6]
_input4 = 3
result4 = 1

print(tests.searchInsert(test1, _input1) == result1)
print(tests.searchInsert(test2, _input2) == result2)
print(tests.searchInsert(test3, _input3) == result3)
print(tests.searchInsert(test4, _input4) == result4)

