class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])

        L, R, ans = 0, len(values) - 1, ""
        while L <= R:
            mid = (L + R) // 2

            if values[mid][1] > timestamp:
                R = mid - 1
            else:
                ans = values[mid][0]
                L = mid + 1
        
        return ans
