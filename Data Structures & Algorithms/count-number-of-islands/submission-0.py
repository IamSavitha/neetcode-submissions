class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #up, down, right , left
        
        max_row = len(grid)
        max_col = len(grid[0])


        island = 0 

        def dfs(y,x):
            if (y < 0 or x < 0 or y >= max_row or x >= max_col or grid[y][x] == "0"):
                return 
            
            grid[y][x] = "0" # marking it has visited 
            for dy, dx in directions:
                dfs(y + dy , x + dx)

        for y in range(max_row):
            for x in range(max_col):
                if grid[y][x] == "1":
                    dfs(y,x)
                    island += 1 

        return island
