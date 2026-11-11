class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, k = 1, max(piles), max(piles)

        while l <= r:
            mid = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += p // mid
                hours += 1 if p % mid != 0 else 0
            
            if hours > h: 
                l = mid + 1
            else:
                k = mid
                r = mid - 1
            
        return k