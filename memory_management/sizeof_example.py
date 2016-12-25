import sys
class mylist:
    """A class that implements __sizeof__"""
    def __init__(self, iterable):
        self.data = list(iterable)

    def __sizeof__(self):
        return object.__sizeof__(self) + \
            sum(sys.getsizeof(v) for v in self.__dict__.values()) + \
            sum(sys.getsizeof(item) for item in self.data)

original_data = [[1,2,3], [1,2,3]]
print(sys.getsizeof(original_data))
foo = mylist(original_data)
print(sys.getsizeof(foo))

