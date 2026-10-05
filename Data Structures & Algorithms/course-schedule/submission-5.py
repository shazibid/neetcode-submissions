class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #this is a building graph kinda problem, build the graph then traverse
        #idea: if we know all the prerecs can be completed (no cycle) then this course can be completed

        #this is our graph :D
        #adjacency list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        #cycle detection dfs
        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): #if cycle detected in prerec
                    return False
                
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
            

