class Sol:
    def get_options(self, priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars) -> int:
        self.num_ways = 0

        options = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]

        self.backtrack(options, dollars, 0)

        return self.num_ways

    def backtrack(self, options, dollars, i):
        if dollars < 0:
            return

        if i >= len(options):
            self.num_ways += 1
            return

        for product in options[i]:
            self.backtrack(options, dollars - product, i + 1)

if __name__ == '__main__':
    solution = Sol()
    assert solution.get_options([2, 3], [4], [2, 3], [1, 2], 10) == 4
    assert solution.get_options([2, 3], [4], [2, 3], [1, 2], 9) == 1
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 12) == 4
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 13) == 8
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 14) == 12
    assert solution.get_options([100], [1, 1, 1, 1], [4, 5, 6], [1], 99) == 0
    assert solution.get_options([1], [1], [1], [1], 4) == 1
    assert solution.get_options([1], [1], [1], [1], 3) == 0
