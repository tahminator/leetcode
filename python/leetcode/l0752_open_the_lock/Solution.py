class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # technically, deadends should never be visited which is = already visited = no go again.
        v = set(deadends)

        if "0000" in v:
            return -1

        q = deque([("0000", 0)])
        v.add("0000")

        while q:
            combination, moves = q.popleft()

            if combination == target:
                return moves

            for i in range(4):
                for direction in [1, -1]:
                    new_value = str((int(combination[i]) + direction) % 10)
                    new_combination = combination[:i] + new_value + combination[i + 1:]

                    if new_combination in v:
                        continue

                    v.add(new_combination)
                    q.append((new_combination, moves + 1))

        return -1




