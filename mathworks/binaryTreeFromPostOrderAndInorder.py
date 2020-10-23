# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = dict()
        self.p_idx = 0
        self.p_idx = len(postorder)-1
        
        
        def buildTree(inorder_map, inorder, i_start, i_end, postorder):
            
            if i_start == i_end:
                return None
            
            root = TreeNode(postorder[self.p_idx])
            self.p_idx -= 1
            
            inorder_idx = inorder_map[root.val]
            
            root.right = buildTree(inorder_map, inorder, inorder_idx+1, i_end, postorder)
            root.left = buildTree(inorder_map, inorder, i_start, inorder_idx, postorder)
            return root
    
        
        
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        
        return buildTree(inorder_map, inorder, 0, len(inorder), postorder)    
