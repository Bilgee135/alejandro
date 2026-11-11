class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R, k = 1, max(piles), max(piles)

        while L <= R:
            mid = L + (R - L) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours > h:
                L = mid + 1
            elif hours <= h:
                k = mid
                R = mid - 1
        
        return k