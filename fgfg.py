# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         r = 0
#         o = x
#         while x > 0:
#             r = r * 10 + x % 10
#             x = x // 10
#         if o == r:
#             print('true')
#         else:
#             print('false')
#
#
#
#
# a = Solution(121)
#

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         rev = 0
#         orig = x
#         while x != 0:
#             rev = rev * 10 + x % 10
#             x //= 10
#         return rev == orig

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        r = 0
        o = x
        while x != 0:
            r = r * 10 + x % 10
            x //= 10
        return o == r
