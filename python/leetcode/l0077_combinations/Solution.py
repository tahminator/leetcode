class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k, i, [], res)
        
    def backtrack(n, k, i, [], res):
        if 
