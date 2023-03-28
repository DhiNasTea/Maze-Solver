import sys

class Node:
    def __init__(self, object, value):
        self.object = object
        self.value = value

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [Node(None, 0)] * (self.maxsize + 1)
        node = Node(None, -1 * sys.maxsize)
        self.Heap[0] = node
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos].value > self.Heap[self.leftChild(pos)].value or
                    self.Heap[pos].value > self.Heap[self.rightChild(pos)].value):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)].value < self.Heap[self.rightChild(pos)].value:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element, value):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = Node(element, value)

        current = self.size

        while self.Heap[current].value < self.Heap[self.parent(current)].value:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i].value) + " LEFT CHILD : " +
                  str(self.Heap[2 * i].value) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1].value))

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
        if self.size == 0:
            return None

        # We have a node that shouldn't be reached
        if self.Heap[self.FRONT].value == self.Heap[0].value:
            return None

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(None, 5)
    minHeap.insert(None, 3)
    minHeap.insert(None, 17)
    minHeap.insert(None, 10)
    minHeap.insert(None, 84)
    minHeap.insert(None, 19)
    minHeap.insert(None, 6)
    minHeap.insert(None, 22)
    minHeap.insert(None, 9)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is " + str(minHeap.remove().value))

