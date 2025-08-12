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
from typing import Optional, List


# https://leetcode.com/problems/length-of-last-word/
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip().rstrip()
#         s = s.split()
#         return len(s[-1])
#
# print(Solution().lengthOfLastWord(s="   Hello   World    "))


# https://leetcode.com/problems/plus-one/
# from typing import List
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) -1, -1, -1):
#             if digits[i] + 1 != 10:
#                 digits[i] = digits[i] + 1
#                 return digits
#
#             digits[i] = 0
#             if i == 0:
#                 return [1] + digits
#         return digits
#
#
# print(Solution().plusOne(digits=[9, 9]))


# https://leetcode.com/problems/missing-number/
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         a = []
#         for i in range(0, len(nums) + 1):
#             a.append(i)
#
#         for j in a:
#             if j not in nums:
#                 return j
#
# print(Solution().missingNumber(nums=[0, 1]))


# https://leetcode.com/problems/climbing-stairs/
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if 1 <= n and n <= 45:
#             a = 0
#             b = 1
#             for i in range(n):
#                 a, b = b, a + b
#             return b
#         else:
#             return 1
#
#
# print(Solution().climbStairs(n=5))


# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            b = nums[:]
            a = b.pop(i)
            if a not in b:
                return a


print(Solution().singleNumber([1, 0, 1]))
