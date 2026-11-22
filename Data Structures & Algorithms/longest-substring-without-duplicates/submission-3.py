class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        freq = [0] * 128

        left = right = 0
        best = 0

        for right in range(n):
            idx = ord(s[right])
            freq[idx] += 1

            while freq[idx] > 1:
                freq[ord(s[left])] -= 1
                left += 1
            
            best = max(best, right - left + 1)

        return best