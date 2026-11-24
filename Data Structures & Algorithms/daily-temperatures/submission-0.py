class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                idx = stack[-1][1]
                res[idx] = i - idx
                stack.pop()
            stack.append((curr, i))
        return res