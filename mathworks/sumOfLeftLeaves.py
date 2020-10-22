# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.left_sum = 0
        
        # KEEP a boolean that is true if its the left child. add to sum if it is a leaf node.
        def sumOfLeft(node, is_left_child):
            if not node:
                return
            if not node.left and not node.right and is_left_child:
                self.left_sum += node.val
            
            sumOfLeft(node.left, True)
            sumOfLeft(node.right, False)
        
        sumOfLeft(root, False)
        
        return self.left_sum
