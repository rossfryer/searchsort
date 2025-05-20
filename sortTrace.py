def bubble_sort_trace(arr):
    print("==== Bubble Sort Trace ====")
    n = len(arr)
    data = arr.copy()
    print(f"{'Pass':<6} {'i':<4} {'j':<4} {'Swap?':<8} {'List'}")
    pass_num = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            swapped = False
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
            print(f"{pass_num:<6} {i:<4} {j:<4} {str(swapped):<8} {data}")
        pass_num += 1
    print("Sorted List:", data)
    print()


def selection_sort_trace(arr):
    print("==== Selection Sort Trace ====")
    n = len(arr)
    data = arr.copy()
    print(f"{'Pass':<6} {'i':<4} {'j':<4} {'min_index':<10} {'Swap':<8} {'List'}")
    pass_num = 1
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
            print(f"{pass_num:<6} {i:<4} {j:<4} {min_index:<10} {'':<8} {data}")
        # After inner loop, swap min
        data[i], data[min_index] = data[min_index], data[i]
        print(f"{'':<6} {'':<4} {'':<4} {'':<10} Swapped   {data}")
        pass_num += 1
    print("Sorted List:", data)
    print()


# Example usage
sample_list_1 = [5, 2, 4, 1, 3]
sample_list_2 = [5, 2, 4, 1, 3]

bubble_sort_trace(sample_list_1)
selection_sort_trace(sample_list_2)
