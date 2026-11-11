class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours > h: 
                l = mid + 1
            else:
                k = min(mid, k)
                r = mid - 1
            
        return k