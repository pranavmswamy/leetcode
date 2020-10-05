# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ''' best way - iterative inorder, break at kth iteration and return element.
        To perform inorder iteratively, keep a stack. 
        1. While node is not none, push node to stack and go to left.
        2. if node becomes none, pop the latest element added from stack, 'process' node, 
        3. go to node.right. Repeat step 1. ... until stack is empty or has marker elt '#'. '''
        
        node = root
        stack = list()
        stack.append('#')
        while stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        
        return -1
