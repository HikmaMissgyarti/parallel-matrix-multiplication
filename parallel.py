from multiprocessing import Pool
import random
import time

SIZE = 500

A = None
B = None


def generate_matrix():
    return [
        [random.randint(1, 10) for _ in range(SIZE)]
        for _ in range(SIZE)
    ]


def init_worker(matrix_a, matrix_b):
    global A, B
    A = matrix_a
    B = matrix_b


def multiply_row(row_index):

    row_result = []

    for j in range(SIZE):

        total = 0

        for k in range(SIZE):
            total += A[row_index][k] * B[k][j]

        row_result.append(total)

    return row_result


def run_parallel():

    matrix_a = generate_matrix()
    matrix_b = generate_matrix()

    start = time.time()

    with Pool(
        processes=4,
        initializer=init_worker,
        initargs=(matrix_a, matrix_b)
    ) as pool:

        pool.map(
            multiply_row,
            range(SIZE)
        )

    elapsed = time.time() - start

    return elapsed