from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        queue = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    queue.append((i,j))
                    grid[i][j]="0"
                    count+=1

                while queue:
                    col,row = queue.popleft()

                    #left
                    if col-1>=0 and grid[col-1][row]=="1":
                        grid[col-1][row]="0"
                        queue.append((col-1,row))

                    #right
                    if col+1<len(grid) and grid[col+1][row]=="1":
                        grid[col+1][row]="0"
                        queue.append((col+1,row))

                    #top
                    if row-1>=0 and grid[col][row-1]=="1":
                        grid[col][row-1]="0"
                        queue.append((col,row-1))

                    #bottom
                    if row+1<len(grid[0]) and grid[col][row+1]=="1":
                        grid[col][row+1]="0"
                        queue.append((col,row+1))
            
        return count
