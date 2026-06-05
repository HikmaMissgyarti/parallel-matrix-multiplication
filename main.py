from sequential import run_sequential
from parallel import run_parallel


def main():

    print("=" * 60)
    print("PARALLEL MATRIX MULTIPLICATION")
    print("=" * 60)

    print("\nRunning Sequential Version...")

    sequential_time = run_sequential()

    print(
        f"Sequential Time: {sequential_time:.2f} seconds"
    )

    print("\nRunning Parallel Version...")

    parallel_time = run_parallel()

    print(
        f"Parallel Time: {parallel_time:.2f} seconds"
    )

    speedup = sequential_time / parallel_time

    print("\nRESULT")
    print("-" * 60)

    print(
        f"Sequential : {sequential_time:.2f} s"
    )

    print(
        f"Parallel   : {parallel_time:.2f} s"
    )

    print(
        f"Speedup    : {speedup:.2f}x"
    )


if __name__ == "__main__":
    main()