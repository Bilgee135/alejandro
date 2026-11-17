class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]
        L, R, ans = 0, len(arr) - 1, ""
        while L <= R:
            mid = (L + R) // 2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                L = mid + 1
            else:
                R = mid - 1

        return ans

