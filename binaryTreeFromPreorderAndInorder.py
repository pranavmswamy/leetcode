# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # IF PREORDER IS THERE, THE ROOT ELT IS THE FIRST ELT.
        # FIND THE POS OF ROOT ELT IN INORDER, THEN
        # ALL ELTS TO LEFT OF IT ARE LEFT SUBTREE
        # ALL ELTS RIGHT OF IT ARE RIGHT SUBTREE.
        # CONTINUE RECURSIVELY.
        
        # base case
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        root_in_inorder = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:root_in_inorder])
        root.right = self.buildTree(preorder, inorder[root_in_inorder+1:])
        return root
    
        
        # TO MAKE IT MORE EFFICICENT, STORE INORDER ELT -> IDX IN A MAP SO YOU DONT HAVE TO FIND IT EVERYTIME.
