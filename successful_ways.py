def find_successful_ways(matrix, w, h):
    count = [[0 for x in range(w)] for y in range(h)]
    for row in range(h):
        count[row][0] = 1
    for column in range(1, w):
        for row in range(h):
            j = column - 1
            while j >= 0:
                for i in range(h):
                    if i == row and j == column - 1:
                        count[row][column] += count[i][j]
                    elif matrix[i][j] == matrix[row][column]:
                        count[row][column] += count[i][j]
                j = j - 1
    return count[0][w - 1] if h == 1 else count[0][w - 1] + count[h - 1][w - 1]


if __name__ == "__main__":
    field = [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"]]
    print(find_successful_ways(field, 3, 3))
