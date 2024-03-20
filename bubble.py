import random
import time
import matplotlib.pyplot as plt

# Function to generate a random dataset
def generate_random_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Bubble sort implementation
def bubble_sort(dataset):
    n = len(dataset)
    comparisons = 0
    swaps = 0
    iterations = 0
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            comparisons += 1
            if dataset[j] > dataset[j+1]:
                swaps += 1
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        iterations += 1
    return comparisons, iterations, swaps

# Function to measure the performance of sorting algorithm
def measure_performance(sort_func, dataset):
    start_time = time.time()
    if sort_func == sort_with_builtin:
        sorted_dataset = sort_func(dataset)
        comparisons, iterations, swaps = 0, 0, 0
    else:
        comparisons, iterations, swaps = sort_func(dataset)
    end_time = time.time()
    execution_time = end_time - start_time
    return comparisons, iterations, swaps, execution_time

# Sorting function using Python's built-in sorting
def sort_with_builtin(dataset):
    return sorted(dataset)

# Function to plot performance metrics
def plot_performance(size, comparisons, iterations, swaps, execution_time, dataset_type):
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    ax[0, 0].bar(dataset_type, comparisons, color='blue')
    ax[0, 0].set_title('Comparisons')
    ax[0, 0].set_ylabel('Count')
    for i, v in enumerate(comparisons):
        ax[0, 0].text(i, v + 0.1, str(v), ha='center')
    ax[0, 1].bar(dataset_type, iterations, color='green')
    ax[0, 1].set_title('Iterations')
    ax[0, 1].set_ylabel('Count')
    for i, v in enumerate(iterations):
        ax[0, 1].text(i, v + 0.1, str(v), ha='center')
    ax[1, 0].bar(dataset_type, swaps, color='orange')
    ax[1, 0].set_title('Swaps')
    ax[1, 0].set_ylabel('Count')
    for i, v in enumerate(swaps):
        ax[1, 0].text(i, v + 0.1, str(v), ha='center')
    ax[1, 1].bar(dataset_type, execution_time, color='red')
    ax[1, 1].set_title('Execution Time')
    ax[1, 1].set_ylabel('Seconds')
    for i, v in enumerate(execution_time):
        ax[1, 1].text(i, v + 0.001, f'{v:.6f}', ha='center')
    for ax_row in ax:
        for axis in ax_row:
            axis.set_xlabel('Dataset Size')
    # Annotation for time complexity and space complexity
    ax[1, 1].annotate('Time Complexity: O(n^2)\nSpace Complexity: O(1)',
                      xy=(0.5, 0.9),
                      xycoords='axes fraction',
                      ha='center',
                      va='center',
                      fontsize=10,
                      bbox=dict(boxstyle="round", alpha=0.1))
    fig.tight_layout()
    plt.show()

# Small dataset
small_dataset_size = 100
small_dataset = generate_random_data(small_dataset_size)

# Measure performance of bubble sort for small dataset
comp_bubble, iter_bubble, swaps_bubble, time_bubble = measure_performance(bubble_sort, small_dataset.copy())

# Large dataset
large_dataset_size = 10000
large_dataset = generate_random_data(large_dataset_size)

# Measure performance of bubble sort for large dataset
comp_bubble_large, iter_bubble_large, swaps_bubble_large, time_bubble_large = measure_performance(bubble_sort, large_dataset.copy())

# Plot performance metrics
plot_performance([small_dataset_size, large_dataset_size],
                 [comp_bubble, comp_bubble_large],
                 [iter_bubble, iter_bubble_large],
                 [swaps_bubble, swaps_bubble_large],
                 [time_bubble, time_bubble_large],
                 ['Small', 'Large'])