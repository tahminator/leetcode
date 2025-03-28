from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, [], res, target)
        return res

    def backtrack(self, candidates, subarray, res, target):
        if target < 0:
            return

        if target == 0:
            res.append(list(subarray))
            return

        for i in range(len(candidates)):
            candidate = candidates[i]
            subarray.append(candidate)
            self.backtrack(candidates[i:], subarray, res, target - candidate)
            subarray.pop()


# print(Solution().combinationSum([2,3,6,7], 7))
