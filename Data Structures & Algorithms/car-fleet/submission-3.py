class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [] # Stack to contain car fleet
        arrivalTimes = [(target - p) / s \
            for p, s in sorted(zip(position, speed), reverse=True)]
            
        for t in arrivalTimes:
            if fleet and fleet[-1] >= t:
                continue
            else:
                fleet.append(t)

        return len(fleet)