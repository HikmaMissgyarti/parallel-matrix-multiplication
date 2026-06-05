import random
import time

SIZE = 500


def generate_matrix():
    return [
        [random.randint(1, 10) for _ in range(SIZE)]
        for _ in range(SIZE)
    ]


def multiply_matrix(A, B):

    result = [[0] * SIZE for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                result[i][j] += A[i][k] * B[k][j]

    return result


def run_sequential():

    A = generate_matrix()
    B = generate_matrix()

    start = time.time()

    multiply_matrix(A, B)

    elapsed = time.time() - start

    return elapsed