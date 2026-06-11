class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        queue = deque()
        count=0
        visited = {}

        if amount ==0:
            return 0

        queue.append([amount,count])
        
        while queue:
            amount, count = queue.popleft() 
            for coin in coins: 
                cur_amount = amount - coin
                if cur_amount < 0:
                    continue
                cur_count=count+1 
                if cur_amount == 0:
                    return cur_count
                elif cur_amount in visited:
                    continue 
                else : 
                    visited[cur_amount] = cur_count
                    queue.append([cur_amount,cur_count]) 
                
        return -1