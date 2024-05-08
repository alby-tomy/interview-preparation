class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1, length1 = self.expand_around_center(s, i, i)
            # Even length palindromes
            palindrome2, length2 = self.expand_around_center(s, i, i + 1)
            
            if length1 > resLen:
                res = palindrome1
                resLen = length1
            if length2 > resLen:
                res = palindrome2
                resLen = length2
        
        return res
    
    def expand_around_center(self, s: str, left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right], right - left - 1
    
sol = Solution()
print(sol.longestPalindrome("abadab"))