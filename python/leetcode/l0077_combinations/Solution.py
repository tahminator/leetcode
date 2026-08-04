class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        c = []

        def f(start: int):
            if len(c) == k:
                res.append(c[:])
                return

            for nu in range(start, n + 1):
                c.append(nu)
                f(nu + 1)
                c.pop()

        f(1)
        return res
