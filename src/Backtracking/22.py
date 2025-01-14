from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur_str: List[str], open_cnt: int, close_cnt: int):
            if len(cur_str) == 2 * n:
                ans.append("".join(cur_str))
                return

            if open_cnt < n:
                cur_str.append("(")
                backtrack(cur_str, open_cnt + 1, close_cnt)
                cur_str.pop()
            if close_cnt < open_cnt:
                cur_str.append(")")
                backtrack(cur_str, open_cnt, close_cnt + 1)
                cur_str.pop()

        backtrack([], 0, 0)
        return ans
    

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans = []

#         def backtrack(cur_str: str, open_cnt: int, close_cnt: int):
#             if len(cur_str) == 2 * n:
#                 ans.append(cur_str)
#                 return

#             if open_cnt < n:
#                 backtrack(cur_str + "(", open_cnt + 1, close_cnt)
            
#             if close_cnt < open_cnt:
#                 backtrack(cur_str + ")", open_cnt, close_cnt + 1)
        
#         backtrack("", 0, 0)
#         return ans