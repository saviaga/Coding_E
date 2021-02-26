class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #1. Search trhough the grid for 1
        #2. Determine for each direction if it is 0 or out of bounds
        
        def countperimeter(grid,i,j):
            count = 0
            if j-1 < 0 or grid[i][j-1] == 0: count+=1 #left
            if j+1 >= len(grid[0]) or grid[i][j+1]==0: count+=1 #right 
            if i-1 < 0 or grid[i-1][j]==0: count+=1 #top
            if i+1 >= len(grid) or grid[i+1][j]==0: count+=1 #bottom
            return count
        
        
        perimeter_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    #count perimeter at this position
                    perimeter_count+= countperimeter(grid,i,j)
                    
        return perimeter_count
        