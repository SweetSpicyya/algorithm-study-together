class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = {}
        length = 0
        odd_flag = False

        if len(s)==1:
            return 1

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
        
        for val in count.values():
            if val %2 ==0:
                length+=val
            else :
                length += val-1
                odd_flag = True
        
        if odd_flag == True:
            length+=1
        
        return length 