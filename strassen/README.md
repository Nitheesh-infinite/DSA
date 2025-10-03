# Problem: strassen

Strassen’s algorithm has a time complexity less than O(n^3). However, it does not perform well for smaller input sizes. In this lab, you will implement both Strassen’s algorithm and the naive algorithm for matrix multiplication to compare their performances.

Implement both the naive matrix multiplication and Strassen’s algorithm, and experimentally determine the value of N (matrix size) at which Strassen’s algorithm becomes faster.

Within your Strassen implementation, consider switching to the naive multiplication when N is smaller than a threshold to avoid overhead. Please also experimentally determine a good value of threshold.


Reference: [Strassen Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)


# Your Task
In `strassen.cpp`, implement:

1. **Naive matrix multiplication** using the standard `O(N^3)` algorithm.
2. **Strassen’s algorithm** using a recursive divide-and-conquer approach.

Compare the performance of both algorithms by measuring their runtimes on randomly generated square matrices of increasing sizes (powers of 2). Identify the smallest value of `N` at which Strassen’s algorithm outperforms the naive method.

# Input/Output

Input (stdin):

None required. The code should automatically:
- Run both algorithms on matrices of sizes `N = 2, 4, 8, 16, 32, ..., 1024` (or up to a reasonable limit).
- Use randomly generated integer matrices (e.g., values in range `[-10, 10]`).

Output (stdout):

Print the runtime (in milliseconds or microseconds) of both algorithms for each tested value of `N`.


# Files to Edit [Do not edit any other files]

- `strassen.cpp`


