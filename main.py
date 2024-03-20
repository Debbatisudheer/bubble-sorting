import time
import random
import sys


# Bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    iterations = 0

    for i in range(n):
        swapped = False  # Flag to track if any swaps are made in this pass
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        iterations += 1
        if not swapped:
            break

    return comparisons, swaps, iterations


# Function to format memory size in a human-readable format
def format_memory(size_bytes):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0


# Function to simulate punching a ball
def punch_ball(dataset):
    new_elements = [random.randint(1, 100) for _ in range(100)]  # Generate 100 random numbers
    dataset.extend(new_elements)  # Add the numbers to the dataset
    start_time = time.time()  # Start time for measuring execution time
    comparisons, swaps, iterations = bubble_sort(dataset)  # Sort the dataset using bubble sort
    end_time = time.time()  # End time
    execution_time = end_time - start_time
    space_occupied = sys.getsizeof(dataset)  # Space occupied by the dataset in bytes
    return execution_time, space_occupied, comparisons, swaps, iterations


# Main function
def main():
    dataset = []  # Initialize dataset
    while True:
        input("Press Enter to punch the ball and increase dataset: ")
        execution_time, space_occupied, comparisons, swaps, iterations = punch_ball(dataset)
        formatted_space_occupied = format_memory(space_occupied)  # Format memory size

        print(
            f"Dataset size: {len(dataset)}, Execution time: {execution_time:.6f} seconds, Space occupied: {formatted_space_occupied}")
        print(f"Number of comparisons: {comparisons}, Number of swaps: {swaps}, Number of iterations: {iterations}")
        print(f"Memory usage: {format_memory(space_occupied)}")  # Display memory usage


if __name__ == "__main__":
    main()