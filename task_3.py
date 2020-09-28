"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
import os
res = {}
result = 0
c = 0

with open("text3.txt","r",encoding="UTF-8") as file:
    for line in file:
        key, value = line.split()
        res[key] = value
        c += 1
        result += int(value)
        if int(value) < 20000:
            print(key)

print(result/c)
