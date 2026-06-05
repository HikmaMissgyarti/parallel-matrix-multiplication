# Parallel Matrix Multiplication Using Python Multiprocessing

## Overview

This project compares the performance of sequential and parallel matrix multiplication using Python. The parallel implementation uses the multiprocessing library to distribute computation across multiple processes.

## Objectives

* Understand the concept of parallel computing.
* Compare sequential and parallel execution times.
* Measure performance improvement using speedup analysis.

## Technologies

* Python 3
* Multiprocessing Library
* GitHub

## Project Structure

```
main.py
sequential.py
parallel.py
```

## Testing Result

| Method     | Execution Time |
| ---------- | -------------- |
| Sequential | 24.48 seconds  |
| Parallel   | 9.60 seconds   |

### Speedup

```
Speedup = Sequential Time / Parallel Time
Speedup = 24.48 / 9.60
Speedup = 1.55x
```

## Conclusion

The parallel implementation successfully reduced execution time by distributing matrix multiplication tasks across multiple processes. The experiment achieved a speedup of approximately 2.55 times compared to the sequential approach.
