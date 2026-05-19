from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        queue = deque()
        dis=[[float('inf')]*len(mat[0]) for _ in range(len(mat))]

        # for _ in range(len(mat)):
        #     row = [float('inf')]*len(mat[0])
        #     dis.append(row)
        
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                if mat[m][n] ==0:
                    dis[m][n] = 0
                    queue.append((m,n))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            cur = queue.popleft()
            
            for dr,dc in directions:
                new_r = cur[0]+dr
                new_c = cur[1]+dc

                if new_r >=0 and new_r<len(mat) and new_c >=0 and new_c<len(mat[0]):
                     if dis[new_r][new_c]==float('inf'):
                        dis[new_r][new_c]= dis[cur[0]][cur[1]]+1
                        queue.append((new_r,new_c))
                   
        
        return dis


