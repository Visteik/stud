raw = input("Введите слова в формате без пробелов: кол-во слов/слово1/слово2/словоn ")
parts = [p.strip() for p in raw.split('/')]
print(parts)
words = parts[1:]
res = []
for i in words:
    if len(i) > 10:
        abbr = f"{i[0]}{len(i) - 2}{i[-1]}"
        res.append(abbr)
    else:
        res.append(i)
print("/".join(res))