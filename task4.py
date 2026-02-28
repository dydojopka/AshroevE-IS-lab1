import re

text = "Безопасность - это самая опасная иллюзия"

# Подготовка текста
clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', text).upper()

# Для квадрата 6x6 нам нужно ровно 36 символов
while len(clean_text) < 36:
    clean_text += "X"
# Если текст длиннее - обрезаем его до 36
clean_text = clean_text[:36]

print(f"Очищенный текст (36 букв): {clean_text}\n")

# Определяем магический квадрат 6x6 (сумма = 111)
magic_square = [
    [35,  1,  6, 26, 19, 24],
    [ 3, 32,  7, 21, 23, 25],
    [31,  9,  2, 22, 27, 20],
    [ 8, 28, 33, 17, 10, 15],
    [30,  5, 34, 12, 14, 16],
    [ 4, 36, 29, 13, 18, 11]
]

# Таблица для расстановки букв
table = [["" for _ in range(6)] for _ in range(6)]

# Идем по числам от 1 до 36
for number in range(1, 37):
    # Находим, в какой строке (r) и столбце (c) стоит это число в магическом квадрате
    found = False
    for r in range(6):
        for c in range(6):
            if magic_square[r][c] == number:
                # Берем букву из текста с индексом (число - 1) и кладем в таблицу
                table[r][c] = clean_text[number - 1]
                found = True
                break
        if found: break

# Вывод таблицы
print("Таблица, заполненная по магическому квадрату:")
print("-" * 25)
for row in table:
    print("| " + " | ".join(row) + " |")
print("-" * 25)

# Считываем результат ПО СТРОКАМ
cipher_text = ""
for r in range(6):
    for c in range(6):
        cipher_text += table[r][c]

print("\nЗашифрованный текст:")
print(cipher_text)