class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums

    def heap_sort(self, arr):
        self.build_max_heap(arr)

        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.max_heapify(arr, 0, i)

    def build_max_heap(self, arr):
        for i in range(len(arr) // 2, -1, -1):
            self.max_heapify(arr, i, len(arr))

    def max_heapify(self, arr, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest, n)
