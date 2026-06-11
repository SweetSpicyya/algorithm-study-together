class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        tmp_array=[]
        output=[]

        def backtracking(candidates, index):
            if sum(tmp_array)==target:
                output.append(tmp_array[:])
                return
            
            if sum(tmp_array)>target:
                return
            
            for now in range(index,len(candidates)):
                tmp_array.append(candidates[now])
                backtracking(candidates,now)
                tmp_array.pop()
                    

        backtracking(candidates,0)
        return output