class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def reaches_at(position: int, speed: int):
            # dist = speed * time
            return (target - position) / speed
        
        pos_sorted = sorted((pos, idx) for idx, pos in enumerate(position))

        stack = []
        for pos, idx in pos_sorted:
            spd = speed[idx]
            a_reaches_at = reaches_at(pos, spd)
            while stack and reaches_at(stack[-1][0], stack[-1][1]) <= a_reaches_at:
                stack.pop()
            stack.append((pos, spd))
        
        return len(stack)