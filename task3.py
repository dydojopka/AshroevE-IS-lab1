import re

text = "Безопасность - это самая опасная иллюзия"
keyword = "ЛИНУКС" 

# Подготовка текста
clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', text).upper()
cols = len(keyword)
rows = (len(clean_text) + cols - 1) // cols  # Вычисляем нужное кол-во строк

# Дополняем текст, чтобы таблица была полной
while len(clean_text) < rows * cols:
    clean_text += "Ъ"

# Создаем порядок перестановки
indexed_keyword = []
for i, char in enumerate(keyword):
    indexed_keyword.append((char, i))

# Сортируем по буквам
indexed_keyword.sort()

# Вычисляем порядок столбцов
column_order = []
for char, original_index in indexed_keyword:
    column_order.append(original_index)

print(f"Алфавитный порядок столбцов слова {keyword}: {column_order}\n")

# Заполняем исходную таблицу ПО СТОЛБЦАМ
source_table = [["" for _ in range(cols)] for _ in range(rows)]
index = 0
for c in range(cols):
    for r in range(rows):
        source_table[r][c] = clean_text[index]
        index += 1

# Создаем НОВУЮ таблицу с переставленными столбцами
final_table = [["" for _ in range(cols)] for _ in range(rows)]
for new_idx, old_idx in enumerate(column_order):
    for r in range(rows):
        final_table[r][new_idx] = source_table[r][old_idx]

# Вывод итоговой таблицы
print("Таблица после перестановки столбцов:")
print("-" * (cols * 4 + 1))
for row in final_table:
    print("| " + " | ".join(row) + " |")
print("-" * (cols * 4 + 1))

# Считывание результата ПО СТРОКАМ
cipher_text = ""
for r in range(rows):
    for c in range(cols):
        cipher_text += final_table[r][c]

print("\nЗашифрованный текст:")
print(cipher_text)