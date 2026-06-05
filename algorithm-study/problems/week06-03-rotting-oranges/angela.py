from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        queue = deque()
        time = 0
        fresh =0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while queue:
            flag = False
            for _ in range(len(queue)):
                row,col = queue.popleft()       
                if row>=0 and row<m and col>=0 and col<n:
                    #left
                    if row-1>=0 and grid[row-1][col]==1:
                        fresh-=1
                        grid[row-1][col]=2
                        queue.append((row-1,col))
                        flag = True
                
                    #right
                    if row+1<m and grid[row+1][col]==1:
                        fresh-=1
                        grid[row+1][col]=2
                        queue.append((row+1,col))
                        flag = True

                    #top
                    if col-1>=0 and grid[row][col-1]==1:
                        fresh-=1
                        grid[row][col-1]=2
                        queue.append((row,col-1))
                        flag = True
                
                    #bottom
                    if col+1<n and grid[row][col+1]==1:
                        fresh-=1
                        grid[row][col+1]=2
                        queue.append((row,col+1))
                        flag = True

            if flag==True:
                time+=1

        if fresh >0:
            return -1
        else : return time

       