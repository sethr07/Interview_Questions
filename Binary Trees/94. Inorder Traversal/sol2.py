# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        res = []

        curr = root

        while True:

            if curr is not None:
                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

            if curr is None and len(stack) == 0:
                break        
        return res
        
