class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        x = prices[0]
        ans = 0
        for i in prices:
            
            x = min(x, i)
            ans = max(ans, i - x)

        return ans