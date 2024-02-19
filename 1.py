class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) >> 1
    
    def left_child(self, i):
        return (i << 1) + 1
    
    def right_child(self, i):
        return (i << 1) + 2
    
    def build_min_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)
    
    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def pop_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

# Example usage:
if __name__ == "__main__":
    # Create a min heap
    min_heap = MinHeap()
    
    # Example with integers
    integer_data = [4, 10, 3, 5, 1]
    min_heap.build_min_heap(integer_data)
    print("Min heap with integers:")
    while min_heap.heap:
        print(min_heap.pop_root(), end=' ')
    print()

    # Example with floats
    float_data = [4.5, 3.2, 1.0, 6.7, 2.8]
    min_heap.build_min_heap(float_data)
    print("\nMin heap with floats:")
    while min_heap.heap:
        print(min_heap.pop_root(), end=' ')
    print()
