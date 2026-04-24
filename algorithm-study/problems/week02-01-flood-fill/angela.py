class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        m = len(image)
        n = len(image[0])

        row=sr
        col=sc

        origin = image[sr][sc]

        if origin == color:
            return image

        def dfs(row,col):

            if  row<0 or row >= m or col<0 or col >= n or image[row][col] != origin :
                return

            image[row][col] = color
            
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        
        dfs(sr,sc)
        return image


        