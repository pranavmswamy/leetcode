# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: TreeNode) -> TreeNode:
        # base cases
        if not node:
            return None
        if not node.left and not node.right:
            return node    
        
        # post-order
        self.invertTree(node.left) # left
        self.invertTree(node.right) # right
        node.left, node.right = node.right, node.left # root - invert subtrees for the current node
        
        return node
        
    # post - order solution.
    # define two base cases
    # go left and right recursively.
    # for current, invert the subtrees.
