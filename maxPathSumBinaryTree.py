# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max_val = float('-inf') # because there are negative values in the tree
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum(root)
        return self.max_val
    
    def max_path_sum(self, root: TreeNode) -> int:
        # base case:
        if not root:
            return 0
        else:
            # POST ORDER
            # max sum of left subtree + cur val
            max_left = root.val + self.max_path_sum(root.left)
            
            # max sum of right subtree + cur val
            max_right = root.val + self.max_path_sum(root.right)
            
            # max sum of left + right + cur subtree
            combined = max_left + max_right - root.val # - root.val because we are adding root.val twice, once for max_left and once for max_right
            
            # update global max val: have to check and update:
            # current self.max_val
            # current root.val, since the single node can have a higher value than all paths
            # left path,
            # right path,
            # combined left and right path
            self.max_val = max(root.val, self.max_val, max_left, max_right, combined)
            
            # return max of cur + left subtree, cur + right subtree, current root val.
            # cant return combined sum because then the path will become closed.
            return max(root.val, max_left, max_right)

# FASTER THAN 97%
