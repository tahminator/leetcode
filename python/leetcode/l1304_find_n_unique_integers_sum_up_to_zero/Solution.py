from typing import List

class Solution:
    """
    pts:
        1. can be any type of array
        2. each element in res must be unique
        3. as long as sum(res) == 0 and len(res) == n, we can pick each element
    sol:
        if n is even, we can just fill an array from -(n // 2) to n // 2. if n is odd, just add an extra 0 to get n - 1 slots to n.
        catch: we must fill the array with the largest even number, so we can have a symmetric amount of each positive and negative value.
        if odd, we just add an 0 to th end

    example:
        n = 5
        [-2, -1, 1, 2, 0]

        n = 4
        [-2, -1, 1, 2]
    """
    def sumZero(self, n: int) -> List[int]:
        isEven = n % 2 == 0

        iterator = n if isEven else n - 1
        res = []
        x = -(n // 2)
        for _ in range(iterator):
            res.append(x)
            x = x + 2 if x == -1 else x + 1

        if not isEven:
            res.append(0)

        return res

print(Solution().sumZero(5))
print()
print(Solution().sumZero(4))
