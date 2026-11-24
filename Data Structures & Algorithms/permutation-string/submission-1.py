class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)
        if n < k:
            return False

        orig_freq = [0] * 26
        freq = [0] * 26

        for i in range(k):
            orig_freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if orig_freq[i] == freq[i])
        if matches == 26:
            return True

        l = 0
        for r in range(k, n):
            idx_r = ord(s2[r]) - ord('a')
            freq[idx_r] += 1
            if freq[idx_r] == orig_freq[idx_r]:
                matches += 1
            elif freq[idx_r] == orig_freq[idx_r] + 1:
                matches -= 1

            idx_l = ord(s2[l]) - ord('a')
            freq[idx_l] -= 1
            if freq[idx_l] == orig_freq[idx_l]:
                matches += 1
            elif freq[idx_l] == orig_freq[idx_l] - 1:
                matches -= 1
            l += 1

            if matches == 26:
                return True

        return False