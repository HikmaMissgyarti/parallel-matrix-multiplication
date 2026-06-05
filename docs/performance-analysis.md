# Performance Analysis

[← Testing & Results](./testing-results.md) | [Next → Conclusion](./conclusion.md)

---

Based on the testing results, the parallel implementation achieved a speedup of approximately 2.55 times compared to the sequential implementation.

The improvement was achieved because the workload was distributed across multiple processes that executed simultaneously.

Although the speedup did not reach 4x, this is expected due to several factors:

* Process creation overhead.
* Communication between processes.
* Resource sharing and synchronization.
* Operating system scheduling.

Despite these limitations, the parallel approach significantly reduced execution time and demonstrated the benefits of parallel computing.
