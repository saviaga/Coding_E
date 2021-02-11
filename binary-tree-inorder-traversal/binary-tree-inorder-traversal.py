# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def IOhelper(root):
            if root != None:
                
                IOhelper(root.left)
                ans.append(root.val)
                IOhelper(root.right)
            
         
        ans=[]
        IOhelper(root)
        return ans
        