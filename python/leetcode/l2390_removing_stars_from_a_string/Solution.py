class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalpha():
                stack.append(c);
                continue

            if stack:
                stack.pop()
            
        return "".join(stack)

print(Solution().removeStars("leet**cod*e"))

