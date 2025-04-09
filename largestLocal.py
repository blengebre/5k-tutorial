class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        maxLocal = [[0 for _ in range(n - 2)] for _ in range(n - 2)]

        for i in range(n - 2):           # row index for top-left of 3x3 window
            for j in range(n - 2):       # col index for top-left of 3x3 window
                max_val = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                maxLocal[i][j] = max_val

        return maxLocal
