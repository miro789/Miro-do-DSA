from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(root, path: List[str]):
            if root is None:
                return
            
            # Append the current node's val to the path
            path.append(str(root.val))

            # if the current node has no children >> add the path to the result
            if root.left is None and root.right is None:
                res.append("->".join(path))

            # recursive visit each child
            dfs(root.left, path)
            dfs(root.right, path)

            # Backtrack: remove the current node's value from the path
            path.pop()
        
        dfs(root, [])
        return res

# Runtime: O(n)
# Space: O(n)