#!/bin/bash

printf "Введите название скрипта"
read script_name
script_name="${script_name:-def.sh}"

cd $HOME
touch ~/$script_name
cat << EOF > "$script_name"
    #!/bin/bash
    echo "Терминал $TERM"
    echo "Язык $LANG"
EOF
cat $script_name

chmod +x "$script_name"
echo "Скрипт создан $script_name"

ls "$HOME/Desktop" && mv "&script_name" "$HOME/Desktop/" || echo "Нет рабочего стола в $HOME"
