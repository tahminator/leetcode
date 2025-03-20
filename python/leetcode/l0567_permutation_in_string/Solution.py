class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter1 = [0 for _ in range(26)]
        counter2 = [0 for _ in range(26)]

        for i, c in enumerate(s1):
            counter1[ord(c) - ord("a")] += 1
            counter2[ord(s2[i]) - ord("a")] += 1


        # Can't just add all of them into a counter and check them, the letters need to be contiguous.
        for i in range(len(s2) - len(s1)):
            if counter1 == counter2:
                return True

            counter2[ord(s2[i + len(s1)]) - ord("a")] += 1
            counter2[ord(s2[i]) - ord("a")] -= 1

        if counter1 == counter2:
            return True





print(Solution().checkInclusion("ab", "eidbaooo"))
