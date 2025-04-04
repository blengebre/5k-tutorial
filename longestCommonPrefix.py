class Solution(object):
    def longestCommonPrefix(self, strs):
        me = ""
        if not strs:
            return me
        for j in range(len(strs[0])):  # Use first string as reference
            for i in range(len(strs) - 1):
                if j >= len(strs[i + 1]) or strs[i][j] != strs[i + 1][j]:
                    return me
            me += strs[0][j]
        return me
