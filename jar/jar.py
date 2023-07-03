class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        if capacity.isalpha() == True:
            raise ValueError
        self._capacity = capacity


    @property
    def size(self):
        return self._size

