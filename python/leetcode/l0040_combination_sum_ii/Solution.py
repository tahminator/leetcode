from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        self.bfs(candidates, [], target, res)
        return res

    def bfs(self, candidates, subarray, target, res):
        if target < 0:
            return

        if target == 0:
            res.append(list(subarray))
            return

        prev = -1
        for i in range(len(candidates)):
            candidate = candidates[i]

            if prev == candidate:
                continue

            subarray.append(candidate)
            self.bfs(candidates[i + 1:], subarray, target - candidate, res)
            subarray.pop()
            prev = candidate

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
