class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(s):
            # Check for 2-digit number with '#'
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])
                result.append(chr(ord('a') + num - 1))
                i += 3  # Skip the two digits and the '#'
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1
        return ''.join(result)
