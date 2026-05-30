class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = {}

        def fibonacci(num):
            if num in memo:
                return memo[num]
            if num==1:
                return 1
            if num==2:
                return 2
            
            memo[num] = fibonacci(num-1)+fibonacci(num-2)

            return memo[num]
        
        return fibonacci(n)
