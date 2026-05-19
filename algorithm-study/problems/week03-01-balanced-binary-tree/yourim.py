from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0

            left = check(node.left)
            if left == -1: return -1

            right = check(node.right)
            if right == -1: return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
r = s.isBalanced(root)
print(r)