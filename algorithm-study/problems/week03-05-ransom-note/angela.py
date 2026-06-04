class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dic = {}

        for letter in magazine:
            dic[letter]= dic.get(letter,0)+1
        
        for letter in ransomNote:
            if letter in dic and dic[letter]>0:
                dic[letter]-=1
            else : return False

        return True
