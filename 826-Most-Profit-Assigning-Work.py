class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        def bs(w, difficulty):
            l, r = 0, len(difficulty) - 1
            best = 0
            while l <= r:
                m = (l + r) // 2
                if difficulty[m] <= w:
                    best = m
                    l = m + 1
                else:
                    r = m - 1
            return best

        # Create a list of pairs (difficulty, profit) and sort by difficulty
        jobs = list(zip(difficulty, profit))
        jobs.sort()

        # Update the profit to be the maximum profit up to that difficulty
        for i in range(1, len(jobs)):
            jobs[i] = (jobs[i][0], max(jobs[i][1], jobs[i-1][1]))

        # Extract sorted difficulties and their corresponding max profits
        sorted_difficulty = [job[0] for job in jobs]
        max_profit = [job[1] for job in jobs]

        res = 0

        # For each worker, find the best job they can do using binary search
        for w in worker:
            if w >= sorted_difficulty[0]:
                idx = bs(w, sorted_difficulty)
                res += max_profit[idx]

        return res