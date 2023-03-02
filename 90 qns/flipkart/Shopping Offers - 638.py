class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        return self._best_price(price, special, needs, {})

    def _best_price(self, prices, deals, needs, memory):
        if tuple(needs) in memory:
            return memory[tuple(needs)]

        min_so_far = 0
        for i, need in enumerate(needs):
            min_so_far += need * prices[i]
        for deal in deals:
            needs_left = self._vector_diff(needs, deal)
            if all(num_item >= 0 for num_item in needs_left):
                min_so_far = min(
                    min_so_far, deal[-1] + self._best_price(prices, deals, needs_left, memory))
        memory[tuple(needs)] = min_so_far

        return min_so_far

    def _vector_diff(self, v1, v2):
        return list(map(lambda x: x[0] - x[1], zip(v1, v2)))
