class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = 0
        best_l, best_r = 0, 0

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                best_l = l + 1
                best_r = r
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                best_l = l + 1
                best_r = r
        
        return s[best_l:best_r]