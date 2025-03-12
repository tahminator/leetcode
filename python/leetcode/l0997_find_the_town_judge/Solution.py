from typing import List
from collections import deque
import copy

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dependencies = {} # of length n
        children = {}

        if n == 1:
            return 1

        for naive, trusted in trust:
            current_dependencies = dependencies.get(trusted, 0) 

            current_dependencies += 1

            dependencies[trusted] = current_dependencies

            current_children = children.get(naive, [])
            
            current_children.append(trusted)

            children[naive] = current_children

        for i in range(1, n + 1):
            if dependencies.get(i, 0) == n - 1 and len(children.get(i, [])) == 0: 
                return i

        return -1



