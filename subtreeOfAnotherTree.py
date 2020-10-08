# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # TRAVERSE TREE IN PREORDER (COULD HAVE DONE BFS, EASIER TO READ, SAME COMPLEXITY)
        # IF CUR NODE == T.VAL, CHECK FOR EQUALITY THROUGH ISEQUAL FN. (O(M))
        # ELSE: RECURSE LEFT, RECURSE RIGHT
        # WORST CASE- O(NM)
        
        if s and t:
            found = False
            if s.val == t.val:
                if self.isEqualTree(s,t):
                    found = True
            found = found or self.isSubtree(s.left, t)
            found = found or self.isSubtree(s.right, t)
            return found
        elif not s and not t:
            return True
        else:
            return False
            
        
        
    
    def isEqualTree(self, a: TreeNode, b: TreeNode) -> bool:
        if a and b:
            current = a.val == b.val
            left = self.isEqualTree(a.left, b.left)
            right = self.isEqualTree(a.right, b.right)
            return current and left and right
        elif not a and not b:
            return True
        else:
            return False


# Another method to do this is convert both trees to string and check for subtree string found in tree string.
