def tokenize(text):
    # Создаем множество разделителей для быстрой проверки.
    separators = set(' \t\n,;:?!()[]{}«»—=')
    
    tokens = []         # Список для итоговых слов
    current_word = ""   # Буфер для накопления текущего слова
    
    # Проходим циклом по индексам от 0 до длины строки
    for i in range(len(text)):
        char = text[i]
        is_separator = False
        
        # 1. Проверяем стандартные разделители
        if char in separators:
            is_separator = True
            
        # 2. Особая проверка для точки
        elif char == '.':
            # Точка - разделитель, ЕСЛИ она НЕ находится между двумя цифрами.
            # Проверяем, что мы не в начале и не в конце строки (чтобы не выйти за границы)
            if i > 0 and i < len(text) - 1:
                # Если слева ИЛИ справа не цифра, то это разделитель
                if not (text[i-1].isdigit() and text[i+1].isdigit()):
                    is_separator = True
            else:
                # Если точка в самом начале или в самом конце — это точно разделитель
                is_separator = True
                
        # 3. Действия в зависимости от того, является ли символ разделителем
        if is_separator:
            # Если буфер не пустой, значит мы накопили слово. 
            # Добавляем его в список и очищаем буфер.
            if current_word:
                tokens.append(current_word)
                current_word = ""
        else:
            # Если символ НЕ разделитель, добавляем его в буфер
            current_word += char
            
    # После окончания цикла проверяем: если в буфере осталось слово 
    # (например, строка не заканчивалась разделителем), добавляем его.
    if current_word:
        tokens.append(current_word)
        
    return tokens

# --- Проверка на примерах из задания ---
print(tokenize("Привет, мир! Как дела?"))
print(tokenize("Жили-были 3.14 раза"))
print(tokenize("s = 'don't'"))
print(tokenize("A...B"))
print(tokenize(""))