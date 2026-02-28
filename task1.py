import re

text = "Безопасность - это самая опасная иллюзия"
rows = 5
cols = 8

# Оставляем только буквы и делаем их заглавными
clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', text).upper()
print(f"Очищенный текст: {clean_text}")

# Если букв меньше, чем ячеек (rows * cols), добавляем 'Х'
while len(clean_text) < rows * cols:
    clean_text += "Х"

# Создание и заполнение таблицы
table = [["" for _ in range(cols)] for _ in range(rows)]

# Заполняем таблицу ПО СТОЛБЦАМ
index = 0
for c in range(cols):
    for r in range(rows):
        table[r][c] = clean_text[index]
        index += 1

# Вывод таблицы(для наглядности)
print(f"\nЗаполнение таблицы ({rows}x{cols}) по столбцам:")
print("-" * (cols * 4 + 1))
for row in table:
    print("| " + " | ".join(row) + " |")
print("-" * (cols * 4 + 1))

# Считывание зашифрованного текста ПО СТРОКАМ
cipher_text = ""
for r in range(rows):
    for c in range(cols):
        cipher_text += table[r][c]

print("\nРезультат (считывание по строкам):")
print(cipher_text)