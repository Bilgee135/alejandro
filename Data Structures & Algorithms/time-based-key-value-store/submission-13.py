class TimeMap:

    def __init__(self):
        """
        {
            "key" : [(timestamp, "value"), ...]
        }
        """
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
            return

        start, prev_val = self.timeMap[key][-1]
        for time in range(start + 1, timestamp):
            self.timeMap[key].append((time, prev_val))

        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap or key not in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ""
        elif timestamp >= self.timeMap[key][-1][0]:
            return self.timeMap[key][-1][1]

        values = self.timeMap[key]
        L, R = 0, len(values) - 1
        while L <= R:
            mid = (L + R) // 2

            if timestamp > values[mid][0]:
                L = mid + 1
            elif timestamp < values[mid][0]:
                R = mid - 1
            else:
                return values[mid][1]


