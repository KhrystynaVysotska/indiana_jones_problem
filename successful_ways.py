from collections import defaultdict
from typing import List, Tuple

INPUT_FILE_NAME = "ijones.in"
OUTPUT_FILE_NAME = "ijones.out"


def read_input_data() -> Tuple[List[List[str]], int, int]:
    with open(INPUT_FILE_NAME, "r") as input_file:
        width, height = [int(parameter) for parameter in input_file.readline().strip().split()]
        corridor = [[letter for letter in row.strip()] for row in input_file.readlines()]
    return corridor, width, height


def write_output_data(ways: int) -> None:
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(ways))


def find_successful_ways(corridor: List[List[str]], width: int, height: int) -> int:
    number_of_ways_to_tile = [[0 for tile in range(width)] for row in range(height)]
    number_of_ways_to_letter = defaultdict(int)

    # there is only one way to get to each tile in the most left column
    for row in range(height):
        tile_letter = corridor[row][0]
        number_of_ways_to_tile[row][0] = 1
        number_of_ways_to_letter[tile_letter] += 1

    for column in range(1, width):
        current_column_letter_ways = defaultdict(int)
        previous_column = column - 1
        for row in range(height):
            tile_letter = corridor[row][column]
            # take into account all possible ways to the tiles leftwards with the same letter
            ways = number_of_ways_to_letter[tile_letter]
            if tile_letter != corridor[row][previous_column]:
                ways += number_of_ways_to_tile[row][previous_column]
            number_of_ways_to_tile[row][column] = ways
            current_column_letter_ways[tile_letter] += ways
        update_ways_to_letters(current_column_letter_ways, number_of_ways_to_letter)

    if height == 1:
        return number_of_ways_to_tile[0][width - 1]
    else:
        return number_of_ways_to_tile[0][width - 1] + number_of_ways_to_tile[height - 1][width - 1]


def update_ways_to_letters(current_column_letter_ways: defaultdict, number_of_ways_to_letter: defaultdict) -> None:
    for tile_letter in current_column_letter_ways:
        number_of_ways_to_letter[tile_letter] += current_column_letter_ways[tile_letter]


if __name__ == "__main__":
    corridor, width, height = read_input_data()
    number_of_successful_ways = find_successful_ways(corridor, width, height)
    write_output_data(number_of_successful_ways)
