class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks) * cars * cars

        while l <= r:
            m = (l + r) // 2

            repaired = self.helper(ranks, cars, m)

            # We found a possible value, which means we should try to go lower and see if we can get a better value.
            if repaired >= cars:
                r = m - 1
            else:
                l = m + 1

        return l


    def helper(self, ranks, cars, time):
        repaired = 0

        for mechanic in ranks:
            repaired += floor((time / mechanic) ** 0.5)

        return repaired
