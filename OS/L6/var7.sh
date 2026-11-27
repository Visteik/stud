#!/bin/bash

printf "Введите название файла "
read file_name
if [ ! -f "$file_name" ] || [ ! -r "$file_name" ] ; then
    echo "Ошибка: файл '$file_name' не существует или недоступен для чтения."
    exit
fi
i=1
until [ -z "$(tail -n +$i "$file_name")" ] ; do    
    line=$(tail -n +$i "$file_name" | head -n 1)
    echo "$i * $line"
    ((i++))
done