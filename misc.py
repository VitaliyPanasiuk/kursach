import random

def generate_card_number():
    # Генерируем BIN (банковский идентификационный номер)
    bin = "400000"
    
    # Генерируем IIN (номер типа карты)
    iin = random.choice(["00", "01", "05", "09"])
    
    # Генерируем ACC (уникальный номер карты)
    acc = "".join([str(random.randint(0, 9)) for _ in range(8)])
    
    # Соединяем все части номера карты вместе
    card_number = bin + iin + acc
    
    return card_number