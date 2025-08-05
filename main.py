# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                nums.sort()
                a = (target - nums[-1]) - 1
                return len(nums) + a

print(Solution().searchInsert(nums=[1,3,5,6], target=5))
