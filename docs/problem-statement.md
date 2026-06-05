# Problem Statement

[← Introduction](./introduction.md) | [Next → Methodology](./methodology.md)

---

Matrix multiplication is a computationally intensive task, especially when dealing with large matrices.

In a sequential approach, all calculations are performed by a single process. As the matrix size increases, the execution time also increases significantly.

Modern computers provide multiple CPU cores that can execute tasks simultaneously. However, without parallelization, these resources are not fully utilized.

The main problem addressed in this project is:

**How can parallel computing reduce the execution time of matrix multiplication compared to the traditional sequential approach?**

To answer this question, the project compares execution times between sequential matrix multiplication and parallel matrix multiplication using Python multiprocessing.
