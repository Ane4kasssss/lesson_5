"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import os
import json
rus_dir = {"One":"Один","Two":"Два", "Three":"Три", "Four":"Четыре" }
file_eng = "text4.txt"
file_rus = "text4_new.txt"
with open("text4.txt", "r",encoding="UTF-8") as file_eng:
    eng_dir = json.load(file_eng)
    print(eng_dir)


with open ("text4_new.txt","w",encoding="UTF-8") as file_rus:
