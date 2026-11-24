class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p_max = piles[0]
        for pile in piles:
            p_max = max(p_max, pile)
        
        l, r = 1, p_max 

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles:
                time += int(-(-pile // mid))
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        return l