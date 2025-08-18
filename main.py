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
# from time import process_time
# from typing import Optional, List
from traceback import print_tb
from typing import List

from Tools.scripts.pathfix import keep_flags


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
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             b = nums[:]
#             a = b.pop(i)
#             if a not in b:
#                 return a
#
#
# print(Solution().singleNumber([1, 0, 1]))



# https://leetcode.com/problems/power-of-three/
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         for i in range(31):
#             if 3 ** i == n:
#                 return True
#             continue
#         return False


# https://leetcode.com/problems/contains-duplicate/
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return not len(set(nums)) == len(nums)
#
#
# print(Solution().containsDuplicate([1, 2, 3, 4]))


# https://leetcode.com/problems/majority-element/
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         a = list(set(nums))
#         for i in a:
#             c = nums.count(i)
#             if c > (len(nums) / 2):
#                 return i
#
#
# print(Solution().majorityElement([2,2,1,1,1,2,2]))


# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         return max((x*3 for x,y,z in zip(num, num[1:], num[2:]) if x==y==z), default='')
#
#
# print(Solution().largestGoodInteger("423523338"))


# https://leetcode.com/problems/power-of-four

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         elif n <= 0:
#             return False
#
#         while n > 4:
#             n /= 4
#
#         if n == 4:
#             return True
#
#         return False
#
# print(Solution().isPowerOfFour(16))


# https://leetcode.com/problems/maximum-69-numbe

# class Solution:
#     def maximum69Number(self, num: int) -> int:
#         s = str(num)
#         a = [int(i) for i in s]
#         a = sorted(a, reverse=True)
#         r = int("".join(map(str, a)))
#         return r
#
#
# print(Solution().maximum69Number(9669))



# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

print(Solution().moveZeroes([1,0,2,0,3]))