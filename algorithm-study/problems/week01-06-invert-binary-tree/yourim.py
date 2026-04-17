# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            current = queue.popleft()

            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root

n1 = TreeNode(1)
n3 = TreeNode(3)
n6 = TreeNode(6)
n9 = TreeNode(9)

n2 = TreeNode(2, left=n1, right=n3)
n7 = TreeNode(7, left=n6, right=n9)

root = TreeNode(4, left=n2, right=n7)


sol = Solution()
result = sol.invertTree(root)
result2 = sol.invertTree2(root)

print(result)
print(result2)




        