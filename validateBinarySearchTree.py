# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def validateBST(self, node, node_min, node_max):
        if node:
            return node.val > node_min and node.val < node_max and self.validateBST(node.left, node_min, node.val) and self.validateBST(node.right, node.val, node_max)
        else:
            return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateBST(root, float('-inf'), float('inf'))

# Beats 99%
