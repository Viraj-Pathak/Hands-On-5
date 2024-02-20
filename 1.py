class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def build_min_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        n = len(self.heap)
        if l < n and self.heap[l] < self.heap[i]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def get_root(self):
        if self.heap:
            return self.heap[0]
        return None

    def pop_root(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root


# Example usage
if __name__ == "__main__":
    # Example with integers
    min_heap = MinHeap()
    min_heap.build_min_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("Min Heap of integers:", min_heap.heap)

    root = min_heap.get_root()
    print("Root:", root)

    popped_root = min_heap.pop_root()
    print("Popped Root:", popped_root)
    print("Heap after popping root:", min_heap.heap)

    # Example with floats
    min_heap_float = MinHeap()
    min_heap_float.build_min_heap([4.5, 1.2, 3.7, 2.1, 16.8, 9.3, 10.6, 14.2, 8.9, 7.4])
    print("\nMin Heap of floats:", min_heap_float.heap)

    root_float = min_heap_float.get_root()
    print("Root:", root_float)

    popped_root_float = min_heap_float.pop_root()
    print("Popped Root:", popped_root_float)
    print("Heap after popping root:", min_heap_float.heap)
