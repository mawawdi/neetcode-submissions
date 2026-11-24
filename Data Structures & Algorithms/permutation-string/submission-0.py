class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        if n < k:
            return False

        orig_freq = [0] * 26
        freq = [0] * 26

        for c in s1:
            orig_freq[ord(c) - ord('a')] += 1
        
        l = 0
        r = k - 1

        for i in range(0, r + 1):
            freq[ord(s2[i]) - ord('a')] += 1

        def check():
            for i in range(26):
                if orig_freq[i] != freq[i]:
                    return False
            return True
        
        if check():
            return True

        while l < n - k:
            freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            freq[ord(s2[r]) - ord('a')] += 1
            if check():
                return True
        
        return False