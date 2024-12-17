class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        max_heap = [(-ord(ch), cnt) for ch, cnt in count.items()]
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            ch, cnt = heapq.heappop(max_heap)
            current_count = min(cnt, repeatLimit)
            res.append(chr(-ch)*current_count)
            if cnt - current_count > 0 and max_heap:
                next_ch, next_cnt = heapq.heappop(max_heap)
                res.append(chr(-next_ch))
                if next_cnt > 1:
                    heapq.heappush(max_heap, (next_ch, next_cnt-1))

                heapq.heappush(max_heap, (ch, cnt-current_count))
        return "".join(res)
            