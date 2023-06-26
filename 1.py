class FlatIterator:
    def __init__(self, list_of_list):
        self.flatten_list = self.flatten(list_of_list)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.flatten_list):
            raise StopIteration
        item = self.flatten_list[self.index]
        self.index += 1
        return item

    @staticmethod
    def flatten(lst):
        flattened = []
        for item in lst:
            if isinstance(item, list):
                flattened.extend(FlatIterator.flatten(item))
            else:
                flattened.append(item)
        return flattened


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

