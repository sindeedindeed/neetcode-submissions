class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heapq.heapify_max(stones)
        while len(stones) > 1:
            max_1 = heapq.heappop_max(stones)
            max_2 = heapq.heappop_max(stones)
            smashed = abs(max_1 - max_2)
            heapq.heappush_max(stones, smashed)
        
        return stones[0]