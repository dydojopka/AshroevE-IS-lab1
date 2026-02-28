alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Зашифрованные сообщения
encrypted_messages = [
    "ЮВПЛШУХ",
    "СФЫЮБШЯФУ"
]

# Перебираем возможные ключи
for n in range(1, len(alphabet)):
    print(f"Ключ n = {n}")
    
    for message in encrypted_messages:
        decrypted = ""
        
        for char in message:
            # Находим позицию буквы
            pos = alphabet.find(char)
            
            # Расшифровка (сдвиг назад)
            new_pos = (pos - n) % len(alphabet)
            decrypted += alphabet[new_pos]
        
        print(f"{message} -> {decrypted}")
    
    print("-" * 40)