# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums, target: int):
        
        if len(nums) == 0:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        first, last = -1, -1

        while left <= right:

            if nums[left] == target and nums[right] == target:
                first = left
                last = right
                break

            if left == target:
                first = left
            
            if right == target:
                last = right
                
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
            
        if nums[left] != target or nums[right] != target:
            return [-1, -1]

        return [first, last]

s = Solution()

print(s.searchRange([2, 2], 3)) # [-1,-1]
print(s.searchRange([0,0,1,1,1,4,5,5], 2)) # [-1,-1]
print(s.searchRange([5,7,7,8,8,10], 8)) # [3,4]
print(s.searchRange([5,7,7,8,8,10], 6)) # [-1,-1]
print(s.searchRange([], 0)) # [-1,-1]
