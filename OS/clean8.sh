#!/bin/bash

printf "Введите имя скрипта для удаления следов "
read del_name

if [ -z "$del_name" ]; then
    del_name="def.sh"
fi

if [ -f "$HOME/Desktop/$del_name" ]; then
    rm "$HOME/Desktop/$del_name"
    echo "Файл $del_name удален с ~/Desktop/"
elif [  -f "$HOME/$del_name" ]; then
    rm "$HOME/$del_name"
    echo "Файл $del_name удален из домашней папки."
else 
    echo "Нет такоо скрипта"
fi