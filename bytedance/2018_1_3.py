import heapq
from collections import defaultdict
import sys

class Solution:
    def pm_ideas(self):
        line=list(map(int,sys.stdin.readline().strip().split()))

        N, M, P = line[0],line[1],line[2]
        ideas = []
        for i in range(P):
            line1 = list(map(int, sys.stdin.readline().strip().split()))
            pm_id, proposal_t, priority, duration = line1[0],line1[1],line1[2],line1[3]
            ideas.append((proposal_t, pm_id, priority, duration, i))
        ideas.sort(reverse=True)

        pm = defaultdict(list)

        res = [0] * P
        coders = [0] * M
        heapq.heapify(coders)
        clock = 0
        available = 0

        while ideas or available > 0:
            coder_clock = heapq.heappop(coders)
            clock = max(clock, coder_clock)
            if available == 0:
                clock = max(clock, ideas[-1][0])

            while ideas and ideas[-1][0] <= clock:
                proposal_t, pm_id, priority, duration, idea_id = ideas.pop()
                heapq.heappush(pm[pm_id], (-priority, duration, pm_id, proposal_t, idea_id))
                available += 1

            candidates = []
            for pm_id, tasks in pm.iteritems():
                if tasks:
                    _, duration, pm_id, proposal_t, idea_id = tasks[0]
                    heapq.heappush(candidates, (duration, pm_id, proposal_t, idea_id))

            if not candidates:
                break

            duration, pm_id, proposal_t, idea_id = heapq.heappop(candidates)
            heapq.heappop(pm[pm_id])
            available -= 1
            res[idea_id] = clock + duration
            heapq.heappush(coders, clock + duration)

        for i in range(P):
            print(res[i])


Solution().pm_ideas()