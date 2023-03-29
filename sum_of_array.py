# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i + j == 10:
#             print(a.index(i), a.index(j))
#
#             a.append(a.index(i))
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i + j == target:
#                     a = []
#                     a.append(sum.index(i))
#                     a.append(sum.index(j))
#                     return a

# class Solution:
#     def __init__(self, nums: list[int], target: int):
#         for i in range(len(self.nums)):
#             for j in range(len(self.nums)):
#                 if i + j == self.target:
#                     return self.sum.index(i), self.sum.index(j)
#
# a = Solution
# print(a.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i + j == target:
                    return sum.index(i), sum.index(j)
a = Solution
print(a.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10 ))


# мои четные попытки решить простую задачку в leetCode
