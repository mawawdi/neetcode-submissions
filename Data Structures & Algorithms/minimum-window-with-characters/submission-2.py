class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        n = len(s)
        orig_freq = [0] * 128
        freq = [0] * 128
        need = 0

        for ch in t:
            idx = ord(ch)
            if orig_freq[idx] == 0:
                need += 1
            orig_freq[idx] += 1
        
        have = 0
        left = best_l = best_r = 0
        best = float('inf')

        for right in range(n):
            r_idx = ord(s[right])
            freq[r_idx] += 1

            if orig_freq[r_idx] and freq[r_idx] == orig_freq[r_idx]:
                have += 1

            while have == need:
                if right - left + 1 < best:
                    best = right - left + 1
                    best_l = left
                    best_r = right
                l_idx = ord(s[left])
                if orig_freq[l_idx] and freq[l_idx] == orig_freq[l_idx]:
                    have -= 1
                freq[l_idx] -= 1
                left += 1

        
        return "" if best == float('inf') else s[best_l:best_r + 1]