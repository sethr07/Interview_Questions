# Time -> 2 minutes

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        # inorder -> left, root, right
        def inOrder(node):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)
        
        inOrder(root)

        return res
