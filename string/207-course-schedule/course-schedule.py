class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        unique_course = set()
        for course, prerequisite in prerequisites:
            adjacency[course].append(prerequisite)
        
        def dfs(course):
            if course in unique_course:
                return False
            if course not in adjacency or adjacency[course]==[]:
                return True

            unique_course.add(course)
            p = adjacency[course]
            for item in p:
                if not dfs(item):
                    return False
            unique_course.remove(course)
            adjacency[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True