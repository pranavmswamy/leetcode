# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        ans = []
        frontier = [root]
        
        while frontier:
            ans.append([node.val for node in frontier])
            children = []
            for node in frontier:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            frontier = children
        
        return ans
