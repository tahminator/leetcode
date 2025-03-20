class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        frequencies = [0 for _ in range(26)]

        l = 0

        for r in range(len(s)):
            frequencies[ord(s[r]) - ord("A")] += 1
            while (r - l + 1) - max(frequencies) > k:
                frequencies[ord(s[l]) - ord("A")] -= 1
                l += 1
                continue

            res = max(res, r - l + 1)

        return res

