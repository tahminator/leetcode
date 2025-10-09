class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        first idea: sort and use binary search. that way we can cut down on an O(n^2) operation down to O(n * logn + nlongn) which will be faster.

        we can sort spells, and then iterate over potions. we can then determine successed by using the middle of spells as a midpoint, and figuring out 
        how many successes to include.
        """

        potions.sort()
        res = [0 for _ in range(len(spells))]

        for i in range(len(spells)):
            spell = spells[i]
            l, r = 0, len(potions) - 1

            while l <= r:
                m = (r + l) // 2

                product = potions[m] * spell

                if product < success: # too low
                    l = m + 1
                elif product >= success: # too high
                    r = m - 1

            res[i] = len(potions) - l

        return res

