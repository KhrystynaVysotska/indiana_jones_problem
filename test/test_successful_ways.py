import unittest

from successful_ways import find_successful_ways


class SuccessfulWaysTest(unittest.TestCase):
    def test_find_successful_ways_for_one_row(self):
        corridor = [["a", "b", "c", "d", "e", "f", "a", "g", "h", "i"]]
        number_of_successful_ways = find_successful_ways(corridor, 10, 1)
        self.assertEqual(2, number_of_successful_ways)

    def test_find_successful_ways_for_multiple_duplicates(self):
        corridor = [["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"]]
        number_of_successful_ways = find_successful_ways(corridor, 7, 6)
        self.assertEqual(201684, number_of_successful_ways)

    def test_find_successful_ways_for_square_matrix(self):
        corridor = [["a", "a", "a"], ["c", "a", "b"], ["d", "e", "f"]]
        number_of_successful_ways = find_successful_ways(corridor, 3, 3)
        self.assertEqual(5, number_of_successful_ways)

    def test_find_successful_ways_for_one_tile(self):
        corridor = [["a"]]
        number_of_successful_ways = find_successful_ways(corridor, 1, 1)
        self.assertEqual(1, number_of_successful_ways)

    def test_find_successful_ways_for_two_duplicated_letters(self):
        corridor = [["a", "b", "b"], ["b", "a", "b"], ["b", "a", "a"]]
        number_of_successful_ways = find_successful_ways(corridor, 3, 3)
        self.assertEqual(10, number_of_successful_ways)

    def test_find_successful_ways_for_two_rows_with_multiple_duplicates(self):
        corridor = [["a", "b", "a", "b", "a", "b"], ["b", "a", "b", "a", "b", "a"]]
        number_of_successful_ways = find_successful_ways(corridor, 6, 2)
        self.assertEqual(178, number_of_successful_ways)


if __name__ == '__main__':
    unittest.main()
