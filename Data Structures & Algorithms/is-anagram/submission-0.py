class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charset = dict()

        for i in range(0, len(s)):
            ch_s = s[i]
            ch_t = t[i]
            charset[ch_s] = charset.get(ch_s, 0) + 1
            charset[ch_t] = charset.get(ch_t, 0) - 1
        
        for _, v in charset.items():
            if v != 0:
                return False

        return True
        