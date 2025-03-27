class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s) - 1):
            curr, next = s[i], s[i + 1]
            sum += abs(ord(curr) - ord(next))

        return sum


