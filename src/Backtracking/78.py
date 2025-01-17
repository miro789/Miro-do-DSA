from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start_idx: int, path: List[int]) -> None:
            # Add the current subset to the result
            res.append(path[:])

            # Explore further adding each number starting from start_idx
            for i in range(start_idx, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         self.backtrackSubsets(nums, result, [], 0)
#         return result
#     def backtrackSubsets(self, nums, result, path, index):
#         # if condition
#         result.append(path[:])
#         #backtrack function
#         for i in range(index, len(nums)):
#             path.append(nums[i])
#             self.backtrackSubsets(nums, result, path, i+1)
#             path.pop()
