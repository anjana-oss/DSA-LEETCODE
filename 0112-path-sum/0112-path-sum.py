# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        def dfs(node,targetsum):
            if node is None:
                return False
             
            target=targetsum-node.val
            if node.right is None and node.left is None:
                if target==0:
                    return True

            return dfs(node.left,target ) or dfs(node.right,target)

        return dfs(root,targetSum)                