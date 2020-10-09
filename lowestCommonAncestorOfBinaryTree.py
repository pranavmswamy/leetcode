# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    

	# ALGORITHM
	# PRE - ORDER
	# TRAVERSE THE TREE IN PREORDER, IF CURRENT ROOT == P OR Q, FOUND = TRUE
	# LEFT = TRAVERSE LEFT,
	# RIGHT = TRAVERSE RIGHT
	# IF TWO OF THREE VARIABLES ARE TRUE, THAT IS THE LOWEST COMMON ANCESTOR
	# RETURN FOUND OR LEFT OR RIGHT - MAKES SURE THAT THE RECURSIVE CALL RETURNS TRUE UPWARDS ALWAYS IF P OR Q IS FOUND.
    def __init__(self):
        self.lca = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find_lca(root, p, q)
        return self.lca
    
    def find_lca(self, root, p, q):
        
        # base case
        if not root:
            return None
        
        foundRoot = False
        # check if root is one of those elts
        if root == p or root == q:
            #print(root.val)
            foundRoot = True
        
        checkLeft = self.find_lca(root.left, p, q)
        checkRight = self.find_lca(root.right, p, q)
        
        #print(checkLeft, checkRight, foundRoot)
        
        if (foundRoot and checkLeft) or (foundRoot and checkRight) or (checkLeft and checkRight):
            self.lca = root
        
        return foundRoot or checkLeft or checkRight
