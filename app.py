import random
import time
import os
import platform

# ==========================================================
# ОЧИСТКА ЭКРАНА
# ==========================================================

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


GREEN = "\033[92m"
RESET = "\033[0m"

# ==========================================================
# DOS-СТИЛЬ ВВОДА (БЛОЧНЫЙ КУРСОР)
# ==========================================================

def dos_input(prompt):
    return input(GREEN + prompt + "█ " + RESET)


# ==========================================================
# ПЛАВНЫЙ ВЫВОД
# ==========================================================

def slow_print(text, delay=0.02):
    for char in text:
        print(GREEN + char + RESET, end="", flush=True)
        time.sleep(delay)
    print()


# ==========================================================
# MATRIX-ДОЖДЬ (ЛЁГКИЙ)
# ==========================================================

def matrix_rain(duration=1.2):
    symbols = "01アイウエオカキクケコABCDEFGHIJKLMNOPQRSTUVWXYZ"
    width = 70

    end_time = time.time() + duration

    while time.time() < end_time:
        line = "".join(random.choice(symbols) for _ in range(width))
        print(GREEN + line + RESET)
        time.sleep(0.05)


# ==========================================================
# КРАСИВАЯ ВИСЕЛИЦА
# ==========================================================

HANGMAN_STAGES = [
    """
     ╔════════════╗
     ║            ║
     ║            
     ║            
     ║            
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║            
     ║            
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║            │
     ║            
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║           ╱│
     ║            
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║           ╱│╲
     ║            
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║           ╱│╲
     ║           ╱ 
     ║            
═════╩════════════╩═════
    """,
    """
     ╔════════════╗
     ║            ║
     ║            O
     ║           ╱│╲
     ║           ╱ ╲
     ║            
═════╩════════════╩═════
    """
]

# ==========================================================
# БОЛТАНИЕ
# ==========================================================

def hanging_animation():
    frames = [
        """
     ╔════════════╗
     ║            ║
     ║           \\O
     ║            │
     ║           ╱ ╲
     ║            
═════╩════════════╩═════
        """,
        """
     ╔════════════╗
     ║            ║
     ║            O
     ║           ╱│╲
     ║           ╱ ╲
     ║            
═════╩════════════╩═════
        """,
        """
     ╔════════════╗
     ║            ║
     ║           O/
     ║            │
     ║           ╱ ╲
     ║            
═════╩════════════╩═════
        """
    ]

    for _ in range(4):
        for frame in frames:
            clear_screen()
            print(GREEN + frame + RESET)
            time.sleep(0.3)


# ==========================================================
# СЛОВА (МНОГО)
# ==========================================================

WORDS = {
    "Обычные слова": [
        {"word": "дом", "hint": "Место, где живут люди"},
        {"word": "кот", "hint": "Домашнее животное"},
        {"word": "собака", "hint": "Лучший друг человека"},
        {"word": "яблоко", "hint": "Популярный фрукт"},
        {"word": "школа", "hint": "Место обучения"},
        {"word": "книга", "hint": "Источник знаний"},
        {"word": "стол", "hint": "Предмет мебели"},
        {"word": "стул", "hint": "На нём сидят"},
        {"word": "река", "hint": "Водный поток"},
        {"word": "лес", "hint": "Много деревьев"},
        {"word": "гора", "hint": "Высокая природная возвышенность"},
        {"word": "море", "hint": "Большой водоём"},
        {"word": "чай", "hint": "Горячий напиток"},
        {"word": "молоко", "hint": "Белый напиток"},
        {"word": "солнце", "hint": "Источник света"},
        {"word": "луна", "hint": "Спутник Земли"},
    ],
    "Программирование": [
        {"word": "python", "hint": "Язык программирования"},
        {"word": "алгоритм", "hint": "Последовательность действий"},
        {"word": "переменная", "hint": "Хранит данные"},
        {"word": "цикл", "hint": "Повторяет код"},
        {"word": "функция", "hint": "Блок кода"},
        {"word": "класс", "hint": "Шаблон объекта"},
        {"word": "объект", "hint": "Экземпляр класса"},
        {"word": "массив", "hint": "Структура данных"},
        {"word": "строка", "hint": "Тип данных для текста"},
        {"word": "компилятор", "hint": "Переводит код"},
        {"word": "интерфейс", "hint": "Способ взаимодействия"},
        {"word": "сервер", "hint": "Обслуживает клиентов"},
    ]
}


# ==========================================================
# ИГРА
# ==========================================================

def choose_category():
    categories = list(WORDS.keys())

    slow_print("Категории:")
    for i, cat in enumerate(categories, 1):
        slow_print(f"{i}. {cat}")

    while True:
        choice = dos_input("Выберите категорию:")
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]


def get_random_word(category):
    selected = random.choice(WORDS[category])
    return selected["word"].upper(), selected["hint"]


def display_game(stage, progress, attempts_left):
    print(GREEN + HANGMAN_STAGES[stage] + RESET)
    slow_print("Слово: " + " ".join(progress))
    slow_print(f"Попыток осталось: {attempts_left}")


def update_word(word, progress, letter):
    for i in range(len(word)):
        if word[i] == letter:
            progress[i] = letter


def play_round():
    clear_screen()
    matrix_rain(1)
    clear_screen()

    category = choose_category()
    word, hint = get_random_word(category)

    progress = ["_" for _ in word]
    wrong = 0
    hint_used = False
    max_wrong = len(HANGMAN_STAGES) - 1

    clear_screen()

    while wrong < max_wrong and "_" in progress:
        display_game(wrong, progress, max_wrong - wrong)

        guess = dos_input("Введите букву или 'подсказка':").upper()

        if guess == "ПОДСКАЗКА":
            if not hint_used:
                slow_print("Подсказка: " + hint)
                hint_used = True
                wrong += 1
            else:
                slow_print("Подсказка уже использована.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            continue

        if guess in word:
            update_word(word, progress, guess)
        else:
            wrong += 1

        clear_screen()

    clear_screen()

    if "_" not in progress:
        slow_print("ACCESS GRANTED")
        time.sleep(0.6)
        slow_print(f"Поздравляю! Это слово: {word}")
    else:
        hanging_animation()
        slow_print("SYSTEM FAILURE")
        slow_print(f"Слово было: {word}")

    time.sleep(1.5)
    clear_screen()


# ==========================================================
# MAIN
# ==========================================================

def main():
    clear_screen()
    matrix_rain(1.5)
    clear_screen()

    slow_print("Hello, Player...")
    slow_print("The Matrix has you...")
    slow_print("Follow the white cursor ...")
    time.sleep(1.5)

    clear_screen()
    slow_print("Вы попали в игру Виселица в Матрице")
    time.sleep(1)
    clear_screen()

    while True:
        slow_print("1. Начать игру")
        slow_print("2. Выход")

        choice = dos_input("Выберите:")

        if choice == "1":
            play_round()
        elif choice == "2":
            slow_print("Disconnecting from Matrix...")
            break


if __name__ == "__main__":
    main()
