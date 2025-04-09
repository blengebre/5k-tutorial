class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = []
        num = len(matrix)
        col = len(matrix[0])  # number of columns

        for j in range(col):  # fix: loop over columns
            arr.append([])    # fix: initialize inner list
            i = 0
            while i < num:
                arr[j].append(matrix[i][j])  # fix: swap i and j for transpose
                i = i + 1
        return arr
