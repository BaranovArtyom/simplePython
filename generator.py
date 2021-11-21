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

# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 **2 и так далее).(Генератор)

def multi_yield(limit):
     for i in range(1, limit+1):
         yield i ** 2

     
multi_obj = multi_yield(5)
for my_string in multi_obj:
    print(my_string)
