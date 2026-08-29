class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self):
        node = self.tail.prev

        if node == self.head:
            return None

        self.remove(node)
        return node

    def empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.nodes = {}

        # frequency -> DoublyLinkedList
        self.freq = {}

        # Minimum frequency currently in cache
        self.min_freq = 0

    def _increase_freq(self, node):
        old_freq = node.freq

        # Remove from old frequency list
        old_list = self.freq[old_freq]
        old_list.remove(node)

        # If this was the minimum-frequency list
        # and it is now empty
        if old_freq == self.min_freq and old_list.empty():
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        # Add to new frequency list
        if node.freq not in self.freq:
            self.freq[node.freq] = DoublyLinkedList()

        self.freq[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        # get increases frequency
        self._increase_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.nodes:
            node = self.nodes[key]

            node.value = value

            # put also increases frequency
            self._increase_freq(node)

            return

        # Cache is full
        if self.size == self.capacity:
            min_list = self.freq[self.min_freq]

            # Remove LRU key from minimum-frequency list
            node = min_list.remove_last()

            del self.nodes[node.key]

            self.size -= 1

        # Insert new key
        node = Node(key, value)

        self.nodes[key] = node

        if 1 not in self.freq:
            self.freq[1] = DoublyLinkedList()

        self.freq[1].add_front(node)

        # New element always has frequency 1
        self.min_freq = 1
        self.size += 1