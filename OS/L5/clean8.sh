#!/bin/bash

printf "Введите имя скрипта для удаления следов "

read del_name
del_name="${del_name:-def.sh}"

p="$(ls "$HOME/Desktop/$del_name" "$HOME/$del_name" 2>/dev/null | head -1)"

: "${p:+$(rm -- "$p")}"

echo "Файл $del_name ${p:+удален: $p}${p:-не найден}"