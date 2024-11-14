class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            return 0 <= int(segment) <= 255 and (segment=="0" or segment[0]!="0")
        
        def dfs(start, parts):
            if len(parts)==4:
                if start==len(s):
                    res.append(".".join(parts))
                return

            for length in range(1,4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        dfs(start+length, parts + [segment])
        res = []
        dfs(0, [])
        return res