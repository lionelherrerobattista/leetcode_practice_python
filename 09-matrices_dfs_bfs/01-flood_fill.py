from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc] # sr, sc -> source row, source column
        height = len(image)
        width = len(image[0])

        def dfs(sr, sc):
            # base cases
            if (0 <= sr < height and # check limits 
                0 <= sc < width and
                image[sr][sc] == current_color and # only change the source node color
                image[sr][sc] != color): # avoid loop
                # update color
                image[sr][sc] = color
                # recursive call
                dfs(sr + 1, sc) # up
                dfs(sr - 1, sc) # down
                dfs(sr, sc + 1) # right
                dfs(sr, sc - 1) # left
            
        dfs(sr, sc)

        return image

