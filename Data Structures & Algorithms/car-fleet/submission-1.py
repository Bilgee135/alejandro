class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeedMap = {pos : spe for pos, spe in zip(position, speed)}
        position.sort(reverse=True)
        stack = []
        
        for i in range(len(position)):
            position[i] = (target - position[i]) / posSpeedMap[position[i]]

        for i in range(len(position)):
            if stack and stack[-1] >= position[i]:
                continue
            else:
                stack.append(position[i])
        
        return len(stack)
