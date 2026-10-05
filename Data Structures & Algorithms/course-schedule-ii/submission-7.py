class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #cycle detection to quickly just return []

        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visiting = set()
        visited = set()

        def dfs(crs): #i want to keep this T/F
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True


        for crs in preMap:
            if not dfs(crs):
                return []
        return res