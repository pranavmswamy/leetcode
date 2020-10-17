# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = list()
        # edge case
        if not root:
            return []
        
        # global variable for keeping track of prev depth.
        self.prev_depth = -1
        
        def right(node, depth):
            # base case
            if not node:
                return
            # current node: if depth is new, it is the right-most node in that level since we are traversing in root-right-left way. So, add to ans.
            # change prevdepth to the new depth so that its siblings dont get added later when the recursive call goes there
            if depth > self.prev_depth:
                self.prev_depth = depth
                ans.append(node.val)
            
            # traverse right first *** important
            right(node.right, depth+1)
            
            # traverse left.
            right(node.left, depth+1)
        
        right(root, 0)
        return ans
                
