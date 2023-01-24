# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(root):
            if root is None:
                return 0
            return max(get_height(root.left), get_height(root.right)) + 1
       
        if root is None:
            return True
        
        lh = get_height(root.left)
        rh = get_height(root.right)

        if (abs(lh - rh) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
            return True

        return False
