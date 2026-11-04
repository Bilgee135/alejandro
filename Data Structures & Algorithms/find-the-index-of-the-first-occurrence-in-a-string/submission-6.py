class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = 0, 0
        ans = -1
        while H < len(haystack):
            if haystack[H] == needle[N]:
                H += 1
                N += 1
                if N == len(needle):
                    return H - N
            else:
                H = H - N + 1
                N = 0

        return ans