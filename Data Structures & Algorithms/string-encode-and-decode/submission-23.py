class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i, length = 0, ""
        while i < len(s):
            if s[i] == "#":
                decoded.append(s[i + 1: i + 1 + int(length)])
                i += int(length) + 1
                length = ""
            else:
                length += s[i]
                i += 1

        return decoded

