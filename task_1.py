"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
import os
some_path = os.path.join(os.path.dirname(__file__),"text1.txt")
with open (some_path, "w", encoding="UTF-8") as file:
    while True:
        vvod = input("Введите данные\n")
        if not vvod:
            break
            file.write(f"vvod\n")

