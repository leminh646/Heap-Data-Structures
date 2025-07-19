# Sorting Algorithms and Benchmark Suite

This repository contains implementations of three classic comparison-based sorting algorithms in Python: Heapsort, Mergesort, and Quicksort—along with a benchmarking script to compare their performance on different input distributions.

## Repository Structure
```
├── heapSort.py # In-place Heapsort implementation
├── mergeSort.py # Functional Mergesort implementation
├── quickSort.py # In-place Quicksort implementation
└── benchmark.py # Script to measure and compare runtimes
```

## Requirements

- Python 3.6 or higher
- (No external libraries beyond the Python standard library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/leminh646/Heap-Data-Structures
   cd heapSort
    ```

2. Running the Heapsort algorrithm
    ```bash
    python3 heapSort.py
    ```
    You should see this
    ```
    Original array: [3, 1, 4, 1, 5, 9, 2, 6, 5]
    Sorted array:   [1, 1, 2, 3, 4, 5, 5, 6, 9]
    ```

3. Benchmark
    The benchmark.py script runs all three algorithms—Heapsort, Mergesort, and Quicksort—on inputs of varying sizes and distributions (random, sorted, reversed).
    ```bash
    python3 benchmark.py
    ```
    By default it tests sizes [1000, 2000, 5000]. To customize:
    ```bash
    python3 benchmark.py --sizes 1000 5000 10000 --seed 42
    ```
    --sizes accepsts a list of integer input sizes
    --seed controls the random generator for reproducibility

    Sample Output
    ```
    === Distribution: random ===
    n=  1000  Heapsort:0.003503s  Mergesort:0.002785s  Quicksort:0.001735s
    n=  2000  Heapsort:0.007833s  Mergesort:0.006122s  Quicksort:0.003606s
    n=  5000  Heapsort:0.022964s  Mergesort:0.017501s  Quicksort:0.010343s

    === Distribution: sorted ===
    n=  1000  Heapsort:0.003750s  Mergesort:0.001928s  Quicksort:0.045459s
    n=  2000  Heapsort:0.008600s  Mergesort:0.004062s  Quicksort:0.182942s
    n=  5000  Heapsort:0.024094s  Mergesort:0.011222s  Quicksort:1.146335s

    === Distribution: reversed ===
    n=  1000  Heapsort:0.003233s  Mergesort:0.002057s  Quicksort:0.044884s
    n=  2000  Heapsort:0.007855s  Mergesort:0.004808s  Quicksort:0.180760s
    n=  5000  Heapsort:0.022094s  Mergesort:0.011414s  Quicksort:1.129815s
    ```

## Algorithm Details

- Heapsort builds a max-heap in O(n) time, then repeatedly extracts the maximum element in O(log n) steps.
- Mergesort recursively divides the array and merges sorted halves in O(n log n) time, using O(n) extra space.
- Quicksort uses a first-element pivot by default, partitioning in place in O(n) per level; its average time is O(n log n) but worst-case is O(n²) on already-sorted data.

Refer to the source comments for detailed docstrings and implementation notes.