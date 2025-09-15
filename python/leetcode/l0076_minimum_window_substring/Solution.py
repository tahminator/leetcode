from collections import Counter

class Solution:
    """
    example:
        s = "ADOBECODEBANC", t = "ABC"
             l
             r
             lr
             l r
             l  r
             l   r
             l    r          ADOBEC found match, longest = ADOBEC, try to remove now 
              l   r          DOBEC already last atleast one of each char, keep moving right
              l    r         DOBECO
              l     r        DOBECOD
              l      r       DOBECODE
              l       r      DOBECODEB
              l        r     DOBECODEBA found match of all chars, longest = ADOBEC, try to remove now
               l       r     OBECODEBA
                l      r     BECODEBA
                 l     r     ECODEBA
                  l    r     CODEBA, longest = CODEBA
                   l   r     ODEBA lost one of each, keep moving right
                   l    r    ODEBA  
                   l     r   ODEBANC found match, move right 
                    l    r   DEBANC, longest = DEBANC
                     l   r   EBANC, longest = EBANC
                      l  r   BANC, longest = BANC
                       l r   ANC, lost match, r is at end and we are no longer in matching phase, exit
                   
    """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        res: str | None = None

        validChars = set(t)
        counter = Counter(t)

        for r in range(len(s)):
            if s[r] in validChars:
                counter[s[r]] -= 1

            while self.checkChars(counter):
                if res is None or len(res) >= (r - l + 1):
                    res = s[l:r + 1]
                if s[l] in validChars:
                    counter[s[l]] += 1
                l += 1

        while self.checkChars(counter):
            if res is None or len(res) >= (r - l + 1):
                res = s[l:r + 1]
            if s[l] in validChars:
                counter[s[l]] -= 1
            l += 1

        return res if res is not None else ""

    def checkChars(self, counter: Counter) -> bool:
        for c in counter:
            count = counter[c]

            if count > 0:
                return False

        return True

# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("aa", "aa"))
