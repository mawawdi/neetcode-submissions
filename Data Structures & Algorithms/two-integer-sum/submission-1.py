class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i in range(0, len(nums)):
            map[target - nums[i]] = i
        
        for i in range(0, len(nums)):
            idx = map.get(nums[i], -1)
            if idx == -1 or idx == i:
                continue
            return [min(i, idx), max(i, idx)]

        return []