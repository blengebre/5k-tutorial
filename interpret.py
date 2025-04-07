class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        li = []
        for i in command:
            li.append(i)
        
        be = []
        ba = {'G': 'G', '()': 'o', '(al)': 'al'}
    
        i = 0
        while i < len(command):
            if command[i] == 'G':
                be.append(ba['G'])
                i += 1
            elif command[i:i+2] == '()':
                be.append(ba['()'])
                i += 2
            elif command[i:i+4] == '(al)':
                be.append(ba['(al)'])
                i += 4
            else:
                i += 1  # Just in case, to avoid infinite loops
        return ''.join(be)
