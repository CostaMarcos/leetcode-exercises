# https://leetcode.com/problems/3sum-closest/description/
# Solution: 2 pointers -- 0(n²)

class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()

        resultSum = nums[0] + nums[1] + nums[2]
        minDiff = float('inf')

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == target:
                    return target

                if sum < target:
                    left += 1
                else:
                    right -= 1
                
                diffToTarget = abs(sum - target)
                if (diffToTarget < minDiff):
                    resultSum = sum
                    minDiff = diffToTarget
        return resultSum


s = Solution()
print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1)) # Expect: 2
print(s.threeSumClosest(nums=[0, 0, 0], target=1)) # Expect: 0
