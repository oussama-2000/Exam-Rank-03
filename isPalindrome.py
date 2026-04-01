class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for i in s:
            if i.isalnum():
                filtered += i
        return filtered[::-1].lower() == filtered.lower()


solution = Solution()
print(solution.isPalindrome("non?"))
