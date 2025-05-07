import random
import time
import matplotlib
matplotlib.use('TkAgg')  # or 'QtAgg'
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

def run_tests():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    trials = 5
    linear_times = []
    binary_times = []

    for size in sizes:
        lin_total = 0
        bin_total = 0
        for _ in range(trials):
            data = generate_list(size)
            target = random.choice(data)  # ensure target is present
            lin_total += linear_search(data, target)
            bin_total += binary_search(data.copy(), target)  # copy to avoid sort modifying original
        linear_times.append(lin_total / trials)
        binary_times.append(bin_total / trials)
        print(f"Size {size}: Linear Avg Time = {linear_times[-1]:.6f}s, Binary Avg Time = {binary_times[-1]:.6f}s")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label='Linear Search', marker='o')
    plt.plot(sizes, binary_times, label='Binary Search', marker='o')
    plt.xlabel('List Size')
    plt.ylabel('Average Search Time (seconds)')
    plt.title('Search Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_tests()