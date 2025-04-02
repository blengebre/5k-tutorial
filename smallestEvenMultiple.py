class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        exa = []
        for i in range(n,n*2+1):  # Start from n and go up to 2*n
            if i % 2 == 0 and i % n == 0:
                exa.append(i)
                break  # Stop once the first even multiple is found
        return exa[0]
