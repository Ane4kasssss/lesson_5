"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os

try:
    with open('text2.txt', 'r', encoding='UTF-8') as file:
        count = 0
        for line in file:
            count += 1
            print(f'строка № {count}, количество слов: {len(line.split())}')
except (FileNotFoundError, TypeError):
    print('файл не существует')