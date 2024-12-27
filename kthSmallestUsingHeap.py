import heapq

# Function to find the kth smallest array element
def kthSmallestUsingHeap(arr, K):
    # Create a max heap (priority queue)
    max_heap = []

    # Iterate through the array elements
    for num in arr:
        # Push the negative of the current element onto the max heap
        heapq.heappush(max_heap, -num)

        # If the size of the max heap exceeds K, remove the largest element
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    # Return the Kth smallest element (top of the max heap, negated)
    return -max_heap[0]