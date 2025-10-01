class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()  # to retrieve nodes in O(1)

        # create dummy nodes
        self.head = Node(0, 0)  # keep track of LRU
        self.tail = Node(0, 0)  # keep track of most recent used node

        # connect nodes
        self.head.next = self.tail
        self.tail.previous = self.head

    def remove(self, node):
        # get previous and next node
        previous = node.previous
        next = node.next
        # remove middle node
        previous.next = next
        next.previous = previous

    def insert(self, node):
        # take the nodes before the tail
        previous = self.tail.previous
        next = self.tail
        # insert new node
        previous.next = node
        next.previous = node
        # link new node with others
        node.previous = previous
        node.next = next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # evict the LRU
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


lru = LRUCache(2)
lru.put(1, 10)
print(lru.get(1))
lru.put(2, 20)
