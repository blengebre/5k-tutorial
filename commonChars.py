class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ka = words[0]
        arr = []

        for char in ka:
            found = True
            for i in range(1, len(words)):
                if char in words[i]:
                    words[i] = words[i].replace(char, '', 1)  # remove used char
                else:
                    found = False
                    break
            if found:
                arr.append(char)

        return arr
