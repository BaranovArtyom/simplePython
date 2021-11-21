def multi_yield():
     # yield_str = "This will print the first string"
     # yield yield_str
     # yield_str = "This will print the second string"
     # yield yield_str
     for i in range(1, 4):
         yield_str = "This will print the " + str(i) + " string"
         yield yield_str

multi_obj = multi_yield()
# print(next(multi_obj))
# print(next(multi_obj))
# print(next(multi_obj))
for my_string in multi_obj:
    print(my_string)

# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 **2 и так далее).

class MySquares:
    """
    класс-итератор
    """

    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration


my_squares = MySquares(5)
for val in my_squares:
    print(val)


def squares_gen(limit):
    """
    функция-генератор
    """
    for i in range(1, limit + 1):
        yield i ** 2


res_squares_gen = squares_gen(5)
for cur_square_val in res_squares_gen:
    print(cur_square_val)

# генераторное выражение
gen_exp = (i ** 2 for i in range(1, 6))
for cur_val in gen_exp:
    print(cur_val)

