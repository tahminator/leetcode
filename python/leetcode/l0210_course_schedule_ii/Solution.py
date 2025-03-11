from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereqs = {}
        courseToNext = {}

        for course, prereq in prerequisites:
            c = courseToPrereqs.get(course, 0)
            c += 1
            courseToPrereqs[course] = c

            nextCourses = courseToNext.get(prereq, [])
            nextCourses.append(course)
            courseToNext[prereq] = nextCourses

        q = deque()
        for course in range(numCourses):
            if course not in courseToPrereqs:
                q.append(course)

        res = []
        while q:
            course = q.popleft()
            res.append(course)

            children = courseToNext.get(course, [])

            for child in children:
                c = courseToPrereqs.get(child)
                c -= 1
                courseToPrereqs[child] = c
                if c == 0:
                    q.append(child)

        return res if len(res) == numCourses else []

solution = Solution()
print(solution.findOrder(2, [[1, 0]]))
