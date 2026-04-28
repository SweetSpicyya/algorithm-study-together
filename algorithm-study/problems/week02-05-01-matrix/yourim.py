from collections import deque
from typing import List

def updateMatrix_naive(self, mat: List[List[int]]) -> List[List[int]]:
    m,n = len(mat), len(mat[0])
    res = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0: continue

            queue = deque([r, c, 0])
            visited = {(r, c)}
            found = False
            while queue:
                curr_r, curr_c, dist = queue.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < m and 0<= nc < n and (nr, nc) not in visited:
                        if mat[nr][nc] == 0:
                            res[r][c] = dist + 1
                            found = True
                            break
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist+1))
                    if found: break


def updateMatrix_bfs(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    queue = deque()

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = -1

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))
    return mat


def updateMatrix_dp(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    inf = m+n

    for r in range(m):
        for c in range(n):
            if mat[r][c] != 0:
                top = mat[r-1][c] if r > 0 else inf
                left = mat[r][c-1] if c > 0 else inf
                mat[r][c] = min(top, left) + 1

    for r in range(m):
        for c in range(n):
            if mat[r][c] != 0:
                bottom = mat[r+1][c] if r < m-1 else inf
                right = mat[r][c+1] if c < n-1 else inf
                mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

    return mat


mat = [[0,0,0],[0,1,0],[1,1,1]]
updateMatrix_bfs(mat)