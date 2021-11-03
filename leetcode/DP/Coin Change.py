

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     result = 0
    #     coin_count = 0
    #     coins.sort()
    #     n = len(coins)
    #     while(result != amount):
    #         prev_result = result
    #         for i in range(n - 1, -1, -1):
    #             if result + coins[i] > amount:
    #                 continue
    #             else:
    #                 result += coins[i]
    #                 coin_count += 1
    #                 break
    #         if prev_result == result:
    #             return -1
    #     return coin_count
    
    def coinChange(self, coins: List[int], amount: int) -> int:  
        coins.sort()
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # if all amount less than amount
        min_element = min(coins)
        
        if amount == 0:
            return 0
        
        if amount < min_element:
            return -1
        
        for local_amount in range(1, coins[n - 1] + 1):
            result = 0
            prev_result = result
            coin_count = 0
            while result != local_amount:
                for i in range(n - 1, -1, -1):
                    if result + coins[i] > local_amount:
                        continue
                    else:
                        result += coins[i]
                        coin_count += 1
                        break
                    
                if prev_result == result:
                    coin_amout = float('inf')
                    break
                    
            if local_amount > amount:
                continue
                
            if coin_count == 0:
                dp[local_amount] = float('inf')
            else:
                dp[local_amount] = coin_count
        
        for i in range(coins[n - 1] + 1, amount + 1):
            min_coins = float('inf')
            for j in range(n):
                if min_coins > dp[i - coins[j]] + 1:
                    min_coins = dp[i - coins[j]] + 1
            dp[i] = min_coins
            
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]