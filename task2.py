import re

text = "Безопасность - это самая опасная иллюзия"
keyword = "ЛИНУКС" # i use arch btw
block_size = 6

# Убираем всё, кроме русских букв, и переводим в верхний регистр
clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', text).upper()

# Дополняем текст буквой 'Х', если он не делится на размер блока
while len(clean_text) % block_size != 0:
    clean_text += "Х"

# Нужно пронумеровать буквы слова по их порядку в алфавите
chars = []
for i in range(len(keyword)):
    chars.append([keyword[i], i])

# Сортируем буквы по алфавиту
chars.sort()

# Создаем список-ключ, где для каждой позиции буквы в слове записан её алфавитный ранг
key = [0] * block_size
for rank in range(len(chars)):
    alphabet_order = rank + 1 # Порядковый номер в алфавите (от 1 до 6)
    original_index = chars[rank][1]
    key[original_index] = alphabet_order

print(f"Ключевое слово: {keyword}")
print(f"Числовой ключ:  {key}")
print(f"Подготовленный текст: {clean_text}\n")

# Процесс шифрования по блокам
print("-" * 40)
print(f"{'Открытый блок':<15} | {'Зашифрованный блок'}")
print("-" * 40)

encrypted_text = ""

# Режем текст на куски по 6 символов
for i in range(0, len(clean_text), block_size):
    block = clean_text[i : i + block_size]
    cipher_block = ""
    
    # Переставляем буквы внутри блока согласно ключу
    for k in key:
        index_in_block = k - 1
        cipher_block += block[index_in_block]
        
    encrypted_text += cipher_block
    print(f"{block:<15} | {cipher_block}")

print("-" * 40)

print("\nИтоговый зашифрованный текст:")
print(encrypted_text)