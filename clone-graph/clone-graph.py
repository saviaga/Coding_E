"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return
        
        stack = [node]
        clone = {}
     

        while stack:
            current = stack.pop()
            if current not in clone:
                
                clone[current] = Node(current.val)
            for neigh in current.neighbors: 
                if not neigh in clone:
                    clone[neigh] = Node(neigh.val)
                    stack.append(neigh)
                clone[current].neighbors.append(clone[neigh])        
        return clone[node]
    
