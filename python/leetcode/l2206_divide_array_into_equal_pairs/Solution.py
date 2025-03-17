class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        We can get to O(n) using a hashset and popping off whenever we run into the number that existed.
        This is because a pair, 2 % 2 == 0, and the same can be said for a number that doesn't exist 0 % 2 == 0, which
        is still technically a "valid" pair. We can utilize that behavior to solve it in one pass instead of 2.
        """
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return len(seen) == 0
