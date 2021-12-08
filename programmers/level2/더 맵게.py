import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville)>= 2:
        if scoville[0] >= K:
            return cnt
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + second*2
        heapq.heappush(scoville, mix)
        cnt+=1
    if scoville[0] >= K:
        return cnt
    return -1
