class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for str in strs:
            anagramCounter = [0] * 26
            for letter in str:
                anagramCounter[ord(letter) - ord("a")] += 1
            sublists[tuple(anagramCounter)].append(str)
        return list(sublists.values())
        
