class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted_version1 = version1.split(".")
        splitted_version2 = version2.split(".")
        m, n = len(splitted_version1), len(splitted_version2)
        # print(m, n)
        if m < n:
            remaining = n - m
            splitted_version1 += ["0"]*remaining
        else:
            remaining = m - n
            splitted_version2 += ["0"]*remaining

        for i in range(len(splitted_version2)):
            if int(splitted_version1[i]) < int(splitted_version2[i]):
                return -1
            elif int(splitted_version1[i]) > int(splitted_version2[i]):
                return 1
        return 0