class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return None
        i = 0
        for a in nums:
            j = 0
            for b in nums:
                if a + b == target and i != j:
                    return [i, j]
                j += 1
            i += 1


solution = Solution()
print(solution.twoSum([5, 5], 10))
