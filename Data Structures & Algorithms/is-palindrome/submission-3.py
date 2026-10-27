class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[^a-zA-Z0-9]" 
        s = re.sub(regex, "", s).lower()
        return s == s[::-1]