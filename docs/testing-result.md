# Testing & Results

[← Implementation](./implementation.md) | [Next → Performance Analysis](./performance-analysis.md)

---

The project was tested by multiplying two large matrices using both sequential and parallel approaches.

## Test Results

| Method     | Execution Time |
| ---------- | -------------- |
| Sequential | 24.48 seconds  |
| Parallel   | 9.60 seconds   |

## Speedup

Speedup = Sequential Time / Parallel Time

Speedup = 24.48 / 9.60

Speedup = 2.55x

## Result Screenshot

![Testing Result](/parallel-matrix-multiplication/images/result.png)

The results show that the parallel implementation completed the computation significantly faster than the sequential implementation.
