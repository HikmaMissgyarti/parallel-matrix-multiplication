# Parallel Matrix Multiplication

---

## Navigation

### Documentation

- [Home](./index.md)
- [Introduction](./introduction.md)
- [Problem Statement](./problem-statement.md)
- [Methodology](./methodology.md)
- [System Architecture](./system-architecture.md)
- [Implementation](./implementation.md)
- [Testing & Results](./testing-result.md)
- [Performance Analysis](./performance-analysis.md)
- [Conclusion](./conclusion.md)

---

## Overview

This project was developed for the Parallel Computing and Distributed Systems course.

The project compares two approaches for matrix multiplication:

* Sequential Matrix Multiplication
* Parallel Matrix Multiplication using Python Multiprocessing

The main objective is to analyze the performance difference between sequential and parallel execution and measure the speedup achieved through parallel computing.

---

## Project Objectives

* Understand the concept of parallel computing.
* Implement matrix multiplication using multiprocessing.
* Compare execution time between sequential and parallel approaches.
* Analyze the performance improvement obtained from parallel processing.

---

## Technologies Used

* Python 3.13.7
* Multiprocessing Library
* GitHub
* GitHub Pages

---

## Project Structure

```text
parallel-matrix-multiplication
│
├── docs
│   ├── index.md
│   ├── introduction.md
│   ├── problem-statement.md
│   ├── methodology.md
│   ├── system-architecture.md
│   ├── implementation.md
│   ├── testing-results.md
│   ├── performance-analysis.md
│   └── conclusion.md
│
├── images
│   ├── architecture.png
│   └── result.png
│
├── main.py
├── sequential.py
├── parallel.py
└── README.md
```

---

## Testing Result

| Method     | Execution Time |
| ---------- | -------------- |
| Sequential | 24.48 seconds  |
| Parallel   | 9.60 seconds   |

### Speedup

**2.55x**

---
