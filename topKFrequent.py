class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        info = {}
        out = []

        for i in nums:
            counter = 0
            for j in nums:
                if i == j:
                    counter += 1
            info[i] = counter

        for key, val in info.items():
            if val >= k:
                out.append(key)
        return out


solution = Solution()
print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))
