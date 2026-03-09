class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)


solution = Solution()
print(solution.isAnagram("racecar", "carrace"))
