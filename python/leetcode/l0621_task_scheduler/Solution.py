from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for task in tasks:
            if task not in counter:
                counter[task] = 0
            counter[task] += 1

        unique_tasks = []
        for key in counter:
            unique_tasks.append(key)

        q = deque(unique_tasks)

        intervals = 0
        completed = {}
        prev = None
        while q:
            task = q.popleft()

            intervals += 1

            counter[task] -= 1

            if counter[task] > 0:
                q.append(task)

        return intervals


print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
