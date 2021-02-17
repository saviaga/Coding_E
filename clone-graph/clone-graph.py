"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        stack = [node]
        n = []
        seen = {node: Node(node.val)} #original -> clone mapping
        
        while stack:
            current = stack.pop()  
           
            for nei in current.neighbors: 
                    if nei not in seen: 
                        seen[nei] = Node(nei.val)
                        stack.append(nei)
                    seen[current].neighbors.append(seen[nei])
        return seen[node] 
    
    
             



            
                
                
                
            
            
        