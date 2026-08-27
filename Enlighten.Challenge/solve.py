# Import sys to allow sys.argv CLI arguments
import sys

# Define the word search function: searches every cell and direction for one word; returns its start/end coordinates, or None if not found.
def find_word(grid, word, rows, cols):
    for row in range(rows):
        for col in range(cols):
            for dr, dc in DIRECTIONS:
                if matches_at(grid, word, row, col, dr, dc ,rows, cols):
                    end_r = row +dr * (len(word)-1)
                    end_c = col +dc * (len(word)-1)
                    return row, col, end_r, end_c
    return None

# Establish the directions to search in, 8 of them.
DIRECTIONS =[
    (0,1), #right
    (0,-1), #left
    (1, 0), #down
    (-1,0), #up
    (1, 1), #dwn-right
    (-1,-1), #up-left
    (1,-1), #dwn-left
    (-1, 1) #up-right
]

# Checks whether `word` matches the grid starting at (row, col) in direction (dr, dc).
# Returns True if every letter matches and stays within the grid's bounds, False otherwise.
def matches_at(grid, word, row, col, dr, dc, rows, cols):
    for i in range(len(word)):
        r =row + dr * i
        c = col + dc * i
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if grid[r][c] != word[i]:
            return False

    return True

# Parse through the .txt file for the grid letters and words and format.
def parse_input(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    first_line = lines[0].strip()
    rows_str, cols_str = first_line.split("x")
    rows = int(rows_str)
    cols = int(cols_str)

    grid = []
    for line in lines[1 :1 + rows]:
        letters = line.strip().split()
        capital_letters = []
        for letter in letters:
            capital_letters.append(letter.upper())
        grid.append(capital_letters)

    words = []
    for line in lines[1 + rows :]:
        word = line.strip()
        words.append(word)
    return grid, rows, cols, words

# Allow for use of any filename as well as format output for "WORD XX:XX" format.
if len(sys.argv) < 2:
    print("Usage: python solve.py <filename>")
else:
    result = parse_input(sys.argv[1])
    grid, rows, cols, words = result

    answers = []
    for word in words:
        answer = find_word(grid, word, rows, cols)
        answers.append(answer)

    for word, answer in zip(words, answers):
        if answer is None:
            print(f"Word {word} Not Found")
        else:
            row, col, end_r, end_c = answer
            print(f"{word} {row}:{col} {end_r}:{end_c}")





