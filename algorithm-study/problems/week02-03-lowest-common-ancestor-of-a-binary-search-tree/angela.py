# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        current = root
        
        def dfs(current, p,q):

            if p.val<current.val and q.val<current.val:
                current = current.left
                return dfs(current, p,q)
            elif p.val>current.val and q.val>current.val:
                current = current.right
                return dfs(current, p,q)
            else : return current

        return dfs(current, p,q)