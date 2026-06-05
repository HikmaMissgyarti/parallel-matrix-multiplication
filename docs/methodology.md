# Methodology

[← Problem Statement](./problem-statement.md) | [Next → System Architecture](./system-architecture.md)

---

This project compares two different approaches to matrix multiplication: sequential processing and parallel processing.

## Sequential Approach

In the sequential approach, matrix multiplication is performed using a single process. Every row and column calculation is executed one by one until the entire result matrix is completed.

This method is simple to implement but requires more execution time because all computations are handled by a single CPU core.

## Parallel Approach

In the parallel approach, the computation is divided into multiple processes using Python's multiprocessing library.

The matrix rows are distributed among four processes. Each process calculates a portion of the result matrix simultaneously.

By executing multiple calculations at the same time, the total execution time can be reduced compared to the sequential approach.

## Performance Measurement

The execution time of both approaches is measured using Python's time module.

The performance improvement is evaluated using the speedup formula:

Speedup = Sequential Time / Parallel Time

A higher speedup value indicates better utilization of parallel computing resources.
