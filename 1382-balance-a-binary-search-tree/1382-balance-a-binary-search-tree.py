# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder_list = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_list.append(node.val)
            inorder(node.right)
        
        inorder(root)

        def build(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = TreeNode(inorder_list[mid])
            
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            
            return node
        
        return build(0, len(inorder_list) - 1)