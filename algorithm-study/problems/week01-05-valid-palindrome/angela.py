# 135ms
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         result = True
#         str1 = ""

#         for i in s:
#             check = i.isalnum()
#             if check == True:
#                 str1+=i
            
#         str1 = str1.lower()

#         #two-pointer
#         right = 0
#         left = len(str1)-1
#         while right < left :
#             if str1[right] == str1[left]:
#                 right+=1
#                 left-=1
#                 continue
#             elif str1[right]!= str1[left]: 
#                 result = False
#                 break;

#         return result

#Better way : 14ms
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = True
        s = s.lower()

        #two-pointer
        right = 0
        left = len(s)-1
        while right < left :
            if s[right].isalnum() == False:
                right +=1
                continue
            
            if s[left].isalnum() == False:
                left -=1
                continue

            if s[right] == s[left]:
                right+=1
                left-=1
                continue
            elif s[right]!= s[left]: 
                result = False
                break

        return result
        
        
    
        
