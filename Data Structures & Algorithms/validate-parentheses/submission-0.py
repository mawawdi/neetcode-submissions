class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in close_to_open:
                if not stack or stack[-1] != close_to_open[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack