import re

def markdown_to_html(md):
    # Разбиваем входной текст на отдельные строки
    lines = md.split('\n')
    result = []
    if md == ' ' or md == '""':
        return md
    for line in lines:
        if line.startswith('#'):
            i = 0
            while i < len(line) and line[i] == '#':
                i += 1
            if i <= 6 and i < len(line) and line[i] == ' ':
                level = i
                content = line[i+1:]
                result.append(f'<h{level}>{content}</h{level}>')
                continue
        content = line        
        content = re.sub(r'`([^`]*)`', r'<code>\1</code>', content)
        content = re.sub(r'\*\*([^*]*)\*\*', r'<b>\1</b>', content)
        if not line.startswith('#'):
            result.append(f'<p>{content}</p>')
        else:
            result.append(content)        
    return result

test_md = input("Введите строку md: ")
print(markdown_to_html(test_md))
