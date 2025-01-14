from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # define palindrome check
        def is_palindrome(word):
            return word == word[::-1] #[start : stop : step]
        
        ans = []
        n = len(s)

        def backtrack(start: int, path: List[str]) -> None:
            # Base case: if reached the end of the string
            if start == n:
                ans.append(path[:])
                return
        
            # Loop through the characters in the string
            for end in range(start + 1, n + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    backtrack(start + len(prefix), path + [prefix])
                    # backtrack(end, path + [prefix])
            
        backtrack(0, [])
        return ans

# Time Complexity: O(2^n * n)
# Space Complexity: O(2^n * n)