
class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cor = 0
        for j in range(len(words)):
            for k in range(j + 1, len(words)):
                if set(words[j]) == set(words[k]):
                    cor = cor + 1
        return cor  # <-- return only after all pairs are checked


        
