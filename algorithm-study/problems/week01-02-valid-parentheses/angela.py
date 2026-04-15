class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
            }

        for i in s :
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if not stack :
                    return False
                pair = stack.pop()
                if hashmap[i] != pair:
                      return False
        
        return not stack 