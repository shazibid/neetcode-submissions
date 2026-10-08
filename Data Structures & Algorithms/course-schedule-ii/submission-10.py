class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        res = []

        visited = set()
        visiting = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True

        for crs in premap:
            if not dfs(crs):
                return []
        
        return res
