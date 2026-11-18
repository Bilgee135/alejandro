class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, k = 1, max(piles), max(piles)

        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1
            
            if hours <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return k