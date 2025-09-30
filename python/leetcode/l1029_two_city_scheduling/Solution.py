from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        - would mean that we should pick left, + would mean that we pick right for that given index.
        """
        n = len(costs)
        res = 0
        diffs = []

        for i in range(len(costs)):
            cost = costs[i]
            diffs.append((cost[0] - cost[1], i))

        diffs.sort(key = lambda x: x[0])

        print(diffs)

        for i in range(len(costs) // 2):
            _, idx1 = diffs[i]
            v = costs[idx1][0]
            res += v

            j = len(costs) - 1 - i
            _, idx2 = diffs[j]
            v2 = costs[idx2][1]
            res += v2

        return res


# print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
