class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        result = []
        for num in nums:
            counter[num] += 1

        for i in range(k):
            most_freq = max(counter, key=counter.get)
            result.append(most_freq)
            del counter[most_freq]

        return result