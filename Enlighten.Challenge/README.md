# Alphabet Soup Word Search Solver

This program parses through a generated word search puzzle and uses a list to identify hidden words in all eight directions (horizontal, vertical and diagonal).

## Requirements
- Python Version: 3.14.5

## Running the program
Run: python solve.py <filename>

For example: python solve.py alphasoup.txt

If no filename is provided, the program prints a usage message instead of running.

## Input file format

The input file must follow this structure:
1. Dimensions of the grid, ROWSxCOLS (e.g. 3x3).
2. Rows of letters in a grid, one row per line, separated by spaces.
3. List of hidden words that are placed inside the grid, one word per line.

### Example:
```
3x3
E S M
C N I
G W D
END
MID

```

## Output Format
For each word found, the program will print the word as well as its start and end coordinates.
- For words not found, it will return "Not Found" to catch errors. Example Below.
### Example:
```

END 2:2 4:2
Word FUN Not Found

```




