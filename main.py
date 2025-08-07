# https://leetcode.com/problems/search-insert-position/
# from typing import List
#
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#             else:
#                 nums.append(target)
#                 nums.sort()
#                 a = (target - nums[-1]) - 1
#                 return len(nums) + a
#
# print(Solution().searchInsert(nums=[1,3,5,6], target=5))


# https://leetcode.com/problems/length-of-last-word/
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip().rstrip()
#         s = s.split()
#         return len(s[-1])
#
# print(Solution().lengthOfLastWord(s="   Hello   World    "))


# https://leetcode.com/problems/plus-one/
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] = digits[i] + 1
                return digits

            digits[i] = 0
            if i == 0:
                return [1] + digits
        return digits


print(Solution().plusOne(digits=[9, 9]))