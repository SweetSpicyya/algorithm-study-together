# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        middle = (left+right)//2

        if n ==1:
            return 1

        while left<right:
            if isBadVersion(middle) :
                right = middle
            else:
                left = middle+1
            
            middle = (left+right)//2
        
        return left