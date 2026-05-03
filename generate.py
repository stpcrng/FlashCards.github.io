import json

# Создаем список из 1000 заглушек для карточек
massive_cards_list = []

for i in range(1, 1001):
    card = {
        "word": f"Word_{i}",
        "translation": f"Перевод_{i}",
        "example": f"This is an example sentence for Word_{i}."
    }
    massive_cards_list.append(card)

# Сохраняем в JSON файл прямо в твою папку проекта
file_path = r"C:\Users\STRNGBBY\Documents\FlashCards\massive_words.json"

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(massive_cards_list, file, ensure_ascii=False, indent=2)

print(f"Успешно создано 1000 карточек в файле: {file_path}")