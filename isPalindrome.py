class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        reversed = new_s[::-1]

        return new_s == reversed


solution = Solution()
print(solution.isPalindrome("non"))
