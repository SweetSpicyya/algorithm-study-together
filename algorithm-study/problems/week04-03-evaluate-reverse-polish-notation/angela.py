class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
    
        stack=[]
        oper = ['+','-','*','/']
        
        for token in tokens:
            if token in oper:
                cal=0
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == '+':
                    cal = num1+num2
                elif token == '-':
                    cal = num1-num2
                elif token == '*':
                    cal = num1*num2
                elif token == '/':
                    cal = int(float(num1)/num2)
                
                stack.append(cal)
            else:
                stack.append(int(token))
            
        return stack.pop()