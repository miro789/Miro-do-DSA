from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        start_idx = 0:             []
        start_idx = 1:    a         b           c
        start_idx = 2: (d e f)   (d e f)     (d e f) 
                  >>  ad ae af   bd be bf    cd ce cf    
        """
        
        # Create hash table mapping digits to corresponding letters
        KEY_BOARD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tvu", "9": "wxyz"}

        ans = []
        if not digits: # digits = ""
            return ans


        def backtrack(start_idx: int, path: List[str]) -> None:
            # Base case: if current path length equals digits length
            if start_idx == len(digits):
                # add the current path to ans
                ans.append("".join(path))
                return
            
            # Get each number in digits
            digit = digits[start_idx]
            # Loop through each character corresponding to the current digit
            for char in KEY_BOARD[digit]: 
                # update the current path
                path.append(char)
                backtrack(start_idx + 1, path)
                path.pop()
            
        backtrack(0, [])
        return ans

# Time Complexity: O(4^n * n)
# Space Complexity: O(4^n * n)