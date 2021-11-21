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
