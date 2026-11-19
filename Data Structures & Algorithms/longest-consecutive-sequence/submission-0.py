class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0

        for n in numset:
            if n - 1 not in numset:
                length = 1
                #[0,3,2,5,4,6,1,1]
                while n+length in numset:
                    length += 1
                best = max(length, best)

        return best