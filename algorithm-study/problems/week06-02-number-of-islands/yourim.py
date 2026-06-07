class Solution:
    def explore_island(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'

        self.explore_island(grid, r-1, c)
        self.explore_island(grid, r+1, c)
        self.explore_island(grid, r, c-1)
        self.explore_island(grid, r, c+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        column = len(grid[0])
        answer = 0
        for r in range(row):
            for c in range(column):

                if grid[r][c] == '1':
                    answer += 1
                    self.explore_island(grid, r, c)

        return answer
