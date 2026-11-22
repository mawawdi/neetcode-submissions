class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        left = 0
        right = 1

        best = 0

        while right < n:
            buy = prices[left]
            sell = prices[right]

            if buy < sell:
                best = max(best, sell - buy)
            else:
                left = right
            
            right += 1
        
        return best
