"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        queue = collections.deque([root])
        clone = collections.defaultdict(Node)
        
        while queue:
            
            for _ in range(len(queue)):
               
                current = queue.popleft()
                clone[current].val= current.val
                for child in current.children:                    
                    clone[child].val = child.val
                    clone[current].children.append(clone[child])
                    queue.append(child)
            
        return clone[root]
            
        
    