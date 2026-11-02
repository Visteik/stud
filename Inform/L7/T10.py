def tokenize(text):
    separators = " \t\n.,;:!?()[]{}\"«»…—–= "
    result = []
    buffer = ""
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        if ch in separators:
            # точка внутри числа: 3.14 — сохраняем её в буфер
            if ch == '.' and buffer and all(c.isdigit() for c in buffer):
                if i + 1 < n and text[i + 1].isdigit():
                    buffer += ch
                    i += 1
                    continue
            # сбрасываем буфер
            if buffer:
                result.append(buffer)
                buffer = ""
            i += 1
            continue

        buffer += ch
        i += 1

    if buffer:
        result.append(buffer)

    return result


print(tokenize("Привет, мир! Как дела?"))
print(tokenize("Жили-были 3.14 раза"))
print(tokenize("s = 'don't'"))
print(tokenize("A...B"))
print(tokenize(""))