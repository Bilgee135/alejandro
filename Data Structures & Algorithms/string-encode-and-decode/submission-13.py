class Solution:

    def encode(self, strs: List[str]) -> str:
        # 'length of string' + '#' (as a delimeter) + string 
        # Sort of an idea to create a simple regex 
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # Underlying idea is to use pointers 
        decoded = []
        pointer = 0 
        length = ""

        while pointer < len(s):
            if s[pointer] == "#":
                decoded.append(s[pointer + 1 : pointer + int(length) + 1])
                pointer += int(length) + 1
                length = ""
            else:
                length += s[pointer]
                pointer += 1
        
        return decoded
