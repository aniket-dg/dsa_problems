class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            pre_req[course].append(prerequisite)

        output = []
        visited, cycle = set(), set()
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            pre = pre_req[course]
            cycle.add(course)
            for crs in pre:
                if not dfs(crs):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output