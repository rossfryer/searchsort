import random
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def generate_list(length):
    return [random.randint(0, length - 1) for _ in range(length)]

def linear_search(arr, target):
    start = time.time()
    found = False
    pos = 0
    while not found and pos < len(arr):
        if arr[pos] == target:
            found = True
        else:
            pos += 1
    end = time.time()
    return end - start

def binary_search(arr, target):
    arr.sort()
    start = time.time()
    low, high = 0, len(arr) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if arr[mid] == target:
            found = True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    end = time.time()
    return end - start

def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    return end - start

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end = time.time()
    return end - start

def python_sort(arr):
    start = time.time()
    arr.sort()  # Uses Timsort
    end = time.time()
    return end - start

def run_tests():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    trials = 3
    linear_times = []
    binary_times = []
    bubble_times = []
    selection_times = []
    python_sort_times = []

    for size in sizes:
        lin_total = bin_total = bub_total = sel_total = py_total = 0
        for _ in range(trials):
            data = generate_list(size)
            target = random.choice(data)

            lin_total += linear_search(data, target)
            bin_total += binary_search(data.copy(), target)
            bub_total += bubble_sort(data.copy())
            sel_total += selection_sort(data.copy())
            py_total += python_sort(data.copy())

        linear_times.append(lin_total / trials)
        binary_times.append(bin_total / trials)
        bubble_times.append(bub_total / trials)
        selection_times.append(sel_total / trials)
        python_sort_times.append(py_total / trials)

        print(f"Size {size}: Linear = {linear_times[-1]:.6f}s, "
              f"Binary = {binary_times[-1]:.6f}s, "
              f"Bubble = {bubble_times[-1]:.6f}s, "
              f"Selection = {selection_times[-1]:.6f}s, "
              f"Python Sort = {python_sort_times[-1]:.6f}s")

    # Plotting
    plt.figure(figsize=(12, 6))
    #plt.plot(sizes, linear_times, label='Linear Search', marker='o')
    #plt.plot(sizes, binary_times, label='Binary Search (includes sort)', marker='o')
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(sizes, python_sort_times, label='Python Built-in Sort', marker='o')
    plt.xlabel('List Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_tests()