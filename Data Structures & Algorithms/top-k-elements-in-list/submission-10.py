class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        result = []
        for num in nums:
            counter[num] += 1

        for i in range(k):
            most_frequent = max(counter, key=counter.get)
            result.append(most_frequent)
            counter.pop(most_frequent)

        return result