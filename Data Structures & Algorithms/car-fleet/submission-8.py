class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Cannot pass each other
        # Car at the front will affect the cars at the back
        # Two factors -> one scalar 
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True) # Car ahead matters
        stack = [] # Contains distint fleet arrivals

        for p, s in pairs:
            arrival = (target - p) / s
            if stack and stack[-1] >= arrival:
                continue
            else:
                stack.append(arrival)

        return len(stack)