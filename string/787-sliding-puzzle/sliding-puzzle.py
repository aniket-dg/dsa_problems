class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        mapping = {
            0: [1, 3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }
        start = "".join([str(num) for row in board for num in row])
        queue = deque([(start, 0)])
        visited = set()
        target = "123450"
        while queue:
            current, moves = queue.popleft()

            if current == target:
                return moves

            zero_index = current.index("0")
            for neighbour in mapping.get(zero_index):
                new_state = list(current)
                new_state[zero_index], new_state[neighbour] = new_state[neighbour], new_state[zero_index]
                new_state = "".join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves+1))

        return -1