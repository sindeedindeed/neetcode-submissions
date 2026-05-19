class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heapq.heapify_max(stones)
        while len(stones) > 1:
            max_1 = heapq.heappop_max(stones)