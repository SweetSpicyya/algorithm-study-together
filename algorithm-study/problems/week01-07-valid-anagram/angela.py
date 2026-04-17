class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        result = True
        hashmap = {}
        
        for i in s :
            hashmap[i] = hashmap.get(i,0)+1
        
        for j in t :
            if j in hashmap :
                hashmap[j]-=1
            else :
                result = False
                break
        
        for val in hashmap.values():
            if val:
                result = False
                break
        
        return result