# Domino-Art
This repository contains an algorithm to determine whether a black-and-white pixel-art image can be tiled with 2×1 dominoes. The algorithm also provides a valid tiling configuration if it exists.

## Input
The input is provided as a list of strings, each string representing a row in the pixel-art image. The characters in the strings are either # (black) or . (white).

## Output
1. If the image can be tiled with dominoes, the output should be a list of strings, each containing four space-separated integers. Each string represents the coordinates (column, row) of the cells that a domino will cover.
2. If the image cannot be tiled, the output should be the string "impossible".

## Solution
1. Graph Construction: Treat each black pixel (#) as a node in a graph. Connect adjacent black pixels with edges.
2. Max Flow Problem: Convert the problem into a max flow problem where finding a max flow will determine if a tiling is possible. Use a bipartite graph approach to connect each pixel to potential domino placements.
3. Max Flow Algorithm: Implement the max flow algorithm to check if the maximum number of matches (domino placements) equals the number of black pixels divided by 2.

## Examples
Diamond input:
  ```sh
  ...#...
  ..###..
  ..###..
  ...#...
```
Diamond output:
```sh
3 0 3 1
2 1 2 2
4 1 4 2
3 2 3 3
```

Invalid UVA input:
```sh
.#...#.#...#..#####.
.#...#.#...#..#...#.
.#...#.#...#..#...#.
.#...#.#...#..#####.
.#...#..#.#...#...#.
.#...#..###...#...#.
..###....#....#...#.
```

Invalid UVA output:
```sh
"impossible"
```
Valid UVA input:
```sh
.#...#.#...#..####..
.#...#.#...#..##.##.
.#...#.#...#..#...#.
.#...#.#...#..#.###.
.#...#..#.#...#...#.
.#####..###...#...#.
..###....#..........
```
Valid UVA output:
```
1 0 1 1
5 0 5 1
7 0 7 1
11 0 11 1
15 0 15 1
17 0 16 0
14 1 14 0
18 1 17 1
1 2 1 3
5 2 5 3
7 2 7 3
11 2 11 3
14 3 14 2
16 3 17 3
18 3 18 2
1 4 1 5
5 4 5 5
2 5 2 6
4 5 4 6
8 5 8 4
10 5 10 4
14 5 14 4
18 5 18 4
3 6 3 5
9 6 9 5





