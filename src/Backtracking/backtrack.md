## 1. Backtracking = DFS on Tree

#### 1.1 Binary Tree Paths

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(root: Optional[TreeNode], path: List[str]):
            if not root:
                return
            
            # Append the current node's val to the path
            path.append(str(root.val))

            # if the current node has no children >> add the path to the result
            if not root.left and not root.right:
                res.append("->".join(path))
            
            # recursive visit each child
            dfs(root.left, path)
            dfs(root.right, path)

            # Backtrack: remove the current node's value from the path
            path.pop()
        
        dfs(root, [])
        return res
```

#### 1.2 Ternay Tree Path (or > 2 nodes)

```python
from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children
        
def ternary_tree_paths(root: Node) -> List[str]:
    res = []
    
    def dfs(node: Node, path: List[str]):
        if not node:
            return
        
        # Append the current node's value to the path
        path.append(str(node.val))

        # If the current node has no children, add the path to the result
        if not node.children: 
            res.append("->".join(path))

        # Recursively visit each child
        for child in node.children:
            if child:
            dfs(child, path)
        
        # Backtrack: remove the current node's value from the path
        path.pop()
        
    dfs(root, [])
    return res
```
