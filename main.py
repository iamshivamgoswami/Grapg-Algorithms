class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if  n<=2:
            return [i for i in range(2)]
        
