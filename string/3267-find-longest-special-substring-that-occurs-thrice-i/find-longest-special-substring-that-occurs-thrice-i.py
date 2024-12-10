class Solution:
    def maximumLength(self, s: str) -> int:
        res = float("-inf")
        for i in range(len(s)):
            for j in range(1, len(s)):
                str_here = s[i:j]
                if str_here == "" or len(set(str_here))!=1:
                    continue
                # print(str_here)
                res_str = []
                for k in range(i, len(s)-len(str_here)+1):
                    # print(s[k: k + len(str_here)], end=" ")
                    res_str.append(s[k: k + len(str_here)])
                str_count_here = res_str.count(str_here)
                print(res_str, res_str.count(res_str[0]))
                if str_count_here >= 3:
                    res = max(res, len(str_here))
                
                # print()
            # break
            print()
        return res if res!=float("-inf") else -1