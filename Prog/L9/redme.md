Оценка 3
Выводим git status, ничего не показывает т.к. изменений нет
![alt text](image.png)
Выводим git log, выводит историю коммитов
![alt text](image-1.png)
Создаем файл Sort и выводит статус. Показывает что можем его закомитить
![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

оценка 3 ветки
![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

![alt text](image-10.png)

![alt text](image-11.png)

загрузил ветку mybranch в github

![alt text](image-13.png)

![alt text](image-12.png)
оценка 4
![alt text](image02.png)

git diff --staged пустой
![alt text](ad.png)
после добавления в staged попали данные в git diff --staged
![alt text](image-12.png)
2 версии файла локально, 1 предзагружена и находится в состоянии stage, с локально внесенными изменениями
![alt text](image22.png)
теперь сществует только 1 версия файла, хранящаяся локально
![alt text](image32.png)
лог изменений после коммита сорт
![alt text](image42.png)
статус после коммита сорт и внесения изменнений в сам файл
старая версия сорт закомитчена и ждет отправки, локально хранится измененная версия
![alt text](image52.png)
после отката коммита была удалена строка с принтом, т.к. была возвращена выгруженная версия
![alt text](image-62.png)
откатили изменения в файле сорт до предылущей версии. Заккомитченая копия осталась без изменений

ff-merge
![alt text](image-14.png)
создал файл greeting.txt закомитил и внес изменения и опять закомитил. СОздал ветку feature/uppercase

![alt text](image-15.png)
изменения внесенные в ветки master не отображаются
![alt text](image-16.png)
Добавьте файл greeting.txt и закоммитьте
Каков вывод git branch?
Каков вывод git log --oneline --graph –all
Переключитесь на главную ветку

![alt text](image-17.png)
ветка слилась с  мастер

![alt text](image-18.png)
все ветки слиты

на 5
![alt text](image-19.png)
создана ветка branch 1. Выполнена команда echo и  заокмичен файл. Переход в мастер, выполнена echo и закоммичен файл.

![alt text](image-20.png)
конфликт при слиянии

![alt text](image-21.png)
статус слияния 

![alt text](image-22.png)
гит лог после коммита 

merge conflict


![alt text](image-23.png)
создал mergesort.py и закоммитил

![alt text](image-24.png)
создал ветку Mergesort-Impl, изменил код в файле мержсорт, закоммитил и вернулся в мастер

![alt text](image-25.png)
заменил mergesort в мастер и вывел лог

![alt text](image-26.png)
конфликты после мержа

![alt text](image-27.png)
взял изменения из второй ветки