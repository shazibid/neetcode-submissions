class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #cycle detection -> directed graph

        #1. dictionary where course is key and value is all prereqs for course
        d = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            d[crs].append(pre)
        
        #visiting courses on the current dfs path
        visiting = set()

        #checking through the course we are currently looking at
        def dfs(course):
            if course in visiting: #we've alr seen course
                return False
            if d[course] == []: #no prereqs
                return True
            
            visiting.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False #if we ever occur a false in the prereqs recursion
                
                #we've explored all nodes in this prereq list
            visiting.remove(course)
            d[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False #if ever returns false
        
        return True
