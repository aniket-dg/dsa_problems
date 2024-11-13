class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n_votes = len(votes)
        total_candidates = len(votes[0])
        memo_dict = defaultdict(lambda: [0]*total_candidates)

        for loc, candidates_votes in enumerate(votes):
            for vote, candidate in enumerate(candidates_votes):
                memo_dict[candidate][vote] += 1

        # sorted_candidates = sorted(memo_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
        sorted_candidates = sorted(memo_dict.keys(), key=lambda x: (memo_dict[x], -ord(x)), reverse=True)

        print(memo_dict)
        return "".join(sorted_candidates)