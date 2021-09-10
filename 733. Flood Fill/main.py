class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(r, c, direction):
            dr, dc = direction[0], direction[1]
            r_new = r + dr
            c_new = c + dc
            
            if 0 <= r_new < m and 0 <= c_new < n:
                if not flooded[r_new][c_new] and image[r_new][c_new] == oldColor:
                    flooded[r_new][c_new] = True
                    image[r_new][c_new] = newColor
                    s.append((r_new, c_new))       
        
        m = len(image)
        n = len(image[0])
        
        flooded = [[False] * n for _ in range(m)]
        flooded[sr][sc] = True
        s = [(sr, sc)]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        
        
        while len(s) != 0:
            r, c = s.pop()
            fill(r, c, (0, 1))
            fill(r, c, (0, -1))
            fill(r, c, (1, 0))
            fill(r, c, (-1, 0))
        
        return image
        