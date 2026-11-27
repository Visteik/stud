#!/bin/bash

# через спец символы
if [ "$#" -ne 3 ]; then
    echo "Ошибка: нужно 3 параметра"
    echo "<имя_файла> <имя_каталога> <число>"
    exit 
fi

file_name="$1"
cat_name="$2"
counter="$3"

# по человечески через ввод вручную

# printf "Введите название файла каталог число через пробелы "
# read file_name cat_name counter

# if [ -z "$file_name" ] || [ -z "$cat_name" ] || [ -z "$counter" ]; then
#     echo "Ошибка: нужно 3 параметра"
#     exit 
# fi

if [ ! -x "$file_name" ] || [ ! -f "$file_name" ]; then
    echo "Файл недоступен для исполнения или не существует"
    exit
fi

if [ ! -d "$cat_name" ]; then
    echo "Каталог не существует"
    exit
fi

i=1
until [ "$i" -gt "$counter" ] ; do

    cp "$file_name" "${cat_name}/${file_name}_$i"
    echo "Создана копия $i"
    ((i++))

done

# tt.txt testik5 2