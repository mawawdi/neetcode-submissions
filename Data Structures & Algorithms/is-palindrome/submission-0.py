class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c for c in s if c.isalnum()).lower()

        i = 0
        j = len(clean) - 1

        # aabbaa
        while (i <= j):
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        
        return True