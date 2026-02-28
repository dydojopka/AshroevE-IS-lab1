alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Пары для анализа
pairs = [
    ("АПЕЛЬСИН", "ТВЧЮОДЫА"),
    ("МАНДАРИН", "ТЁУЙЁЦОУ")
]

for plain, cipher in pairs:
    print(f"Анализ пары: {plain} - {cipher}")
    
    # Берем первые буквы
    char_p = plain[0]
    char_c = cipher[0]
    
    # Находим их позиции в алфавите
    pos_p = alphabet.find(char_p)
    pos_c = alphabet.find(char_c)
    
    # Вычисляем сдвиг (n)
    # Если позиция шифробуквы меньше, добавляем длину алфавита (циклический сдвиг)
    n = (pos_c - pos_p) % len(alphabet)
    
    print(f"1. Буква '{char_p}' (позиция {pos_p}) стала '{char_c}' (позиция {pos_c})")
    print(f"2. Вычисленный ключ (сдвиг n) = {n}")
    
    # Проверка по второй букве
    test_pos = (alphabet.find(plain[1]) + n) % len(alphabet)
    if alphabet[test_pos] == cipher[1]:
        print(f"3. Проверка пройдена: для второй буквы ключ тоже подходит.")
    
    print("-" * 30)