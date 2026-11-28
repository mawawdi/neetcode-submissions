class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        half = total_sum // 2
        
        dp = set()
        dp.add(0)

        for num in nums:
            nextdp = set()
            for t in dp:
                nextdp.add(t + num)
                nextdp.add(t)
            dp = nextdp
        
        return True if half in dp else False
