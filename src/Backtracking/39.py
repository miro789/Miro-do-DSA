from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtracking(start_idx: int, remaining: int, path: List[int]) -> None:
            # Base case: if remaining sum is 0, add the current path to the result
            if remaining == 0:
                res.append(path[:])
                return

            # loop through the candidates starting from the current index
            for i in range(start_idx, n): # i = 0 -> n - 1
                curr_val = candidates[i]

                # If the remaining sum is less than the current candidate, skip the rest
                if remaining - curr_val < 0:
                    break
                
                # Include the candidate in the current path and continue searching
                path.append(curr_val)
                backtracking(i, remaining - curr_val, path)
                path.pop() # Backtrack by removing the last added candidate
        
        backtracking(0, target, [])
        return res