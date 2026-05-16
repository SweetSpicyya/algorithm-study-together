# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node):
            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)
           
            if left_h==-1 or right_h==-1 or abs(left_h-right_h)>1:
                return -1

            return 1+max(left_h,right_h)

        if dfs(root) == -1:
            return False
        else:
            return True