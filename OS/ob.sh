#!/bin/bash
echo "   Тип оболочки: $SHELL"
echo "   UID      = $UID"
echo "   USER     = $USER"
echo "   BASH     = $BASH"
echo "   HOME     = $HOME"
echo "   PATH     = $PATH"
echo "   PS1      = $PS1"
echo "   PS2      = $PS2"
echo "   PWD      = $PWD"
echo "   TERM     = $TERM"
echo "   HOSTNAME = $HOSTNAME"
echo "   SECONDS  = $SECONDS"
cd $HOME
cd Lab4/
cat f3
printf "Введите команду"
read user_command
if [ -z "$user_command" ]; then
    echo " ничего не ввели "
else
    eval "$user_command"
fi
