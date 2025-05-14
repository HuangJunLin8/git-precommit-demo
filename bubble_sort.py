def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"Swapping {arr[j]} and {arr[j+1]}")  # 调试代码
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([5, 3, 8, 1, 2]))  # 调试代码
