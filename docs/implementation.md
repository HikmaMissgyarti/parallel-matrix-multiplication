# Implementation

The project is implemented using Python and the multiprocessing library.

## Main Program

The main program is responsible for:

* Running the sequential implementation.
* Running the parallel implementation.
* Measuring execution time.
* Calculating speedup.
* Displaying the final results.

## Sequential Implementation

The sequential implementation performs matrix multiplication using a single process.

All matrix calculations are executed one after another until the result matrix is completed.

File:

```text
sequential.py
```

## Parallel Implementation

The parallel implementation uses Python's multiprocessing library.

The matrix rows are divided among four worker processes. Each process calculates a portion of the result matrix simultaneously.

File:

```text
parallel.py
```

## Performance Measurement

Execution time is measured using Python's time module.

The speedup is calculated by comparing the sequential execution time and the parallel execution time.
