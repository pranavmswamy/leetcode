"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# RECURSIVE APPROACH.
# Iterative approach would be similar to bfs or dfs.

class Solution:
    
    def __init__(self):
        self.new_nodes = dict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # base case
        if not node: return None
        
        # create new node
        head = Node(node.val)
        # add new node to visited/new_nodes dict.
        self.new_nodes[head.val]  = head
        
        # loop through the old copy's neighbors - 
        for neighbor in node.neighbors:
            
            # if it is not visited, recurse by sending the old copy.
            if neighbor.val not in self.new_nodes:
                head.neighbors.append(self.cloneGraph(neighbor))
            # else if it already visited, new copy is created, so just append to neighbors. 
            else:
                head.neighbors.append(self.new_nodes[neighbor.val])
        
        # return head for recursion.
        return head
