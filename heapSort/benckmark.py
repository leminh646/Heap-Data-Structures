import random
import time
import argparse
from heapSort import heapsort
from mergeSort import mergesort
from quickSort import quicksort

def benchmark(sizes, seed=0):
    random.seed(seed)
    distributions = ['random', 'sorted', 'reversed']
    algorithms = {
        'Heapsort': heapsort,
        'Mergesort': mergesort,
        'Quicksort': quicksort
    }

    for dist in distributions:
        print(f"=== Distribution: {dist} ===")
        for n in sizes:
            base = random.sample(range(n * 10), n)
            if dist == 'sorted':
                arr = sorted(base)
            elif dist == 'reversed':
                arr = sorted(base, reverse=True)
            else:
                arr = base
            times = {}
            for name, func in algorithms.items():
                arr_copy = arr.copy()
                start = time.perf_counter()
                # Mergesort returns a new list
                if name == 'Mergesort':
                    func(arr_copy)
                else:
                    func(arr_copy)
                end = time.perf_counter()
                times[name] = end - start
            print(f"n={n:6d}  " +
                  "  ".join(f"{name}:{times[name]:.6f}s" for name in algorithms))
        print()

def main():
    parser = argparse.ArgumentParser(description="Benchmark sorting algorithms.")
    parser.add_argument(
        '--sizes', nargs='+', type=int,
        default=[1000, 2000, 5000],
        help="List of input sizes to test (default: 1000 2000 5000)"
    )
    parser.add_argument(
        '--seed', type=int, default=0,
        help="Random seed for reproducibility (default: 0)"
    )
    args = parser.parse_args()
    benchmark(args.sizes, seed=args.seed)

if __name__ == '__main__':
    main()