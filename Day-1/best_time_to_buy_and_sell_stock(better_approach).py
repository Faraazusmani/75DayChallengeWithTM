class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        arr = []
        for j in range(len(prices)):
            if prices[i] >= prices[j]:
                i = j
                j += 1
            elif prices[i] < prices[j]:
                arr.append(prices[j] - prices[i])
                j += 1
        
        if len(arr) != 0:
            return max(arr)
        else:
            return 0