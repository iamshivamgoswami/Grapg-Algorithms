class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, c: int) -> List[List[int]]:

        def func(a, r, c, fill, prev):
            rows = len(a)
            cols = len(a[0])
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if a[r][c] != prev:
                return
            a[r][c] = fill
            func(a, r - 1, c, fill, prev)
            func(a, r + 1, c, fill, prev)
            func(a, r, c - 1, fill, prev)
            func(a, r, c + 1, fill, prev)

        if c != image[sr][sc]:
            func(image, sr, sc, c, image[sr][sc])
        return image


