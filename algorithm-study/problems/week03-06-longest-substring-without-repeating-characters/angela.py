class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        len_sub = 0

        left=0
        right=0
        visited={}

        if not s :
            return 0
        elif len(s) ==1:
            return 1

        for index,now in enumerate(s):
            if now not in visited:
                visited[now]=index
                right+=1
            else:
                if visited.get(now)+1 > left:
                    left=visited.get(now)+1

                right+=1
                visited[now]=index
            
            len_sub = max(len_sub,right-left)

        return len_sub
        