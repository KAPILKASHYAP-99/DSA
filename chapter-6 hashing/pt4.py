#  chapter - Double hashing
# Double hashing is an open addressing collision resolution technique in hashing.
# If collision occurs at the main hash index, we use a second hash function (h2) to calculate the step size for probing the next index.
# It reduces clustering and gives better distribution.

class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 6 - (key % 6)  # Ensure this never returns 0

    def insert(self, key):
        index = self.h1(key)
        if self.table[index] is None:
            self.table[index] = key
        else:
            i = 1
            new_index = (index + i * self.h2(key)) % self.size
            while self.table[new_index] is not None:
                i += 1
                new_index = (index + i * self.h2(key)) % self.size
            self.table[new_index] = key

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


hash_table = DoubleHashing(7)
hash_table.insert(49)
hash_table.insert(56)
hash_table.insert(72)
hash_table.display()


