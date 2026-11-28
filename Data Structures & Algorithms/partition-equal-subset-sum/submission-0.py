class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        half = total_sum // 2
        
        dp = set()
        dp.add(0)

        for i in range(n - 1, -1, -1):
            nextdp = set()
            for t in dp:
                nextdp.add(t + nums[i])
                nextdp.add(t)
            dp = nextdp
        
        return True if half in dp else False
