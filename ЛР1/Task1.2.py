# TODO Найдите количество книг, которое можно разместить на дискете
memory_capacity_megabyte = 1.44
memory_capacity_byte = memory_capacity_megabyte * 1024 * 1024
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25
symbol_weight = 4
book_weight_byte = number_of_pages * number_of_lines * number_of_symbols * symbol_weight
number_of_books = memory_capacity_byte // book_weight_byte
x = int(number_of_books)
print("Количество книг, помещающихся на дискету:", x)
