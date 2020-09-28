"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
import random
some_path = os.path.join(os.path.dirname(__file__),"text5.txt")
some_numbers = [random.randint(1,50) for _ in range(100)]
print(sum(some_numbers))
with open(some_path,"w", encoding="UTF-8") as file:
    some_str = " ".join(map(str,some_numbers))
    file.write(some_str)
with open(some_path, "r", encoding="UTF-8") as file:
    numbers = map(int, file.read().split(" "))
print(sum(numbers))
