from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original_color = image[sr][sc]
        if original_color == color:
            return image

        def update_color(new_sr, new_sc):
            if not (0 <= new_sr < len(image) and 0 <= new_sc < len(image[0])):
                return
            if image[new_sr][new_sc] != original_color:
                return

            image[new_sr][new_sc] = color
            print(image[new_sr][new_sc])

            update_color(new_sr-1, new_sc)
            update_color(new_sr+1, new_sc)
            update_color(new_sr, new_sc-1)
            update_color(new_sr, new_sc+1)

        update_color(sr, sc)
        return image


### 공간 복잡도 줄인 버전
from collections import deque

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color  # 방문 표시(색칠)

    while queue:
        r, c = queue.popleft()

        # 상하좌우 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image

image = [[0,1,1],[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

s = Solution()
new = s.floodFill(image, sr, sc, color)
print(new)