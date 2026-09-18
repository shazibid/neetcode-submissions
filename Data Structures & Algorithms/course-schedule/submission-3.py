class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs

        #track the prereqs for every course, if ever has itself as a prereq, then return false
        #if there is ever a cycle, return false

        #for each courses, make a map of all the prerecs
        courses = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courses[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            #if we've seen crs
            if crs in visited:
                return False
            #if not prereqs
            if courses[crs] == []:
                return True
            
            #create seen set
            visited.add(crs)
            #for all prerex in course
            for pre in courses[crs]:
                #if dfs on pre returns False
                if not dfs(pre):
                    return False

            
            visited.remove(crs)
            courses[crs] = []
            return True
        
        for crs in courses:
            if not dfs(crs):
                return False
        
        return True
                


        