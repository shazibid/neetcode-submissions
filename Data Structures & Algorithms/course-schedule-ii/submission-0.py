class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #same approach to the last problem
        #as you're popping from the visited, add to res
        courses = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courses[crs].append(pre)
        
        visited = set()
        res = []
        cycle = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in courses[crs]:
                if not dfs(pre): return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res