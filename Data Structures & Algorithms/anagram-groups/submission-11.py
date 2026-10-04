class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for str in strs:
            charCount = [0] * 26 # because input is only lowercase characters
            for c in str:
                charCount[ord(c) - ord('a')] += 1

            result[tuple(charCount)].append(str)

        return list(result.values())