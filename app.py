import random

# ASCII-арт для виселицы
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
       -
    """
]

# Список слов для угадывания
WORDS = [
    "python", "программирование", "компьютер", "алгоритм", "функция",
    "переменная", "цикл", "условие", "массив", "строка",
    "класс", "объект", "наследование", "полиморфизм", "инкапсуляция",
    "база данных", "сервер", "клиент", "протокол", "интерфейс",
    "библиотека", "фреймворк", "отладка", "тестирование", "рефакторинг"
]


def get_random_word():
    """Возвращает случайное слово из списка."""
    return random.choice(WORDS).upper()


def display_game_state(stage, word_progress, guessed_letters, attempts_left):
    """Отображает текущее состояние игры."""
    print("\n" + "=" * 50)
    print(HANGMAN_STAGES[stage])
    print(f"\nСлово: {' '.join(word_progress)}")
    print(f"Осталось попыток: {attempts_left}")
    
    if guessed_letters:
        print(f"Угаданные буквы: {', '.join(sorted(guessed_letters))}")
    print("=" * 50)


def get_player_input(guessed_letters):
    """Получает и валидирует ввод игрока."""
    while True:
        guess = input("\nВведите букву или слово целиком: ").strip().upper()
        
        if not guess:
            print("Пожалуйста, введите что-нибудь.")
            continue
        
        if not guess.isalpha():
            print("Пожалуйста, вводите только буквы.")
            continue
        
        if len(guess) == 1 and guess in guessed_letters:
            print(f"Вы уже называли букву '{guess}'. Попробуйте другую.")
            continue
        
        return guess


def update_word_progress(word, word_progress, guess):
    """Обновляет прогресс слова при угаданной букве."""
    new_progress = list(word_progress)
    
    for i, letter in enumerate(word):
        if letter == guess:
            new_progress[i] = guess
    
    return new_progress


def play_round():
    """Играет один раунд виселицы."""
    word = get_random_word()
    word_progress = ['_'] * len(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_STAGES) - 1
    
    print("\n" + "🎮 ДОБРО ПОЖАЛОВАТЬ В ИГРУ ВИСЕЛИЦА! 🎮")
    print(f"Загадано слово из {len(word)} букв.")
    print("У вас есть 7 попыток, чтобы угадать слово.")
    
    while wrong_guesses < max_wrong and '_' in word_progress:
        display_game_state(wrong_guesses, word_progress, guessed_letters, 
                          max_wrong - wrong_guesses)
        
        guess = get_player_input(guessed_letters)
        
        if len(guess) > 1:
            if guess == word:
                word_progress = list(word)
                print(f"\n🎉 Поздравляем! Вы угадали слово: {word}!")
                return True
            else:
                print(f"\n❌ Неправильно! Слово '{guess}' не загадано.")
                wrong_guesses += 1
                continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            occurrences = word.count(guess)
            word_progress = update_word_progress(word, word_progress, guess)
            print(f"\n✅ Правильно! Буква '{guess}' встречается {occurrences} раз(а).")
        else:
            wrong_guesses += 1
            print(f"\n❌ Неправильно! Буквы '{guess}' нет в слове.")
    
    display_game_state(wrong_guesses, word_progress, guessed_letters, 0)
    
    if '_' not in word_progress:
        print(f"\n🎉 Поздравляем! Вы угадали слово: {word}!")
        return True
    else:
        print(f"\n💀 Вы проиграли! Загаданное слово было: {word}")
        return False


def main():
    """Главная функция игры."""
    print("=" * 50)
    print("      КОНСОЛЬНАЯ ИГРА ВИСЕЛИЦА (HANGMAN)")
    print("=" * 50)
    
    stats = {"played": 0, "won": 0, "lost": 0}
    
    while True:
        won = play_round()
        
        stats["played"] += 1
        if won:
            stats["won"] += 1
        else:
            stats["lost"] += 1
        

        print(f"\n📊 Статистика: сыграно {stats['played']}, "
              f"побед {stats['won']}, поражений {stats['lost']}")
        

        while True:
            again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
            if again in ('да', 'д', 'yes', 'y'):
                break
            elif again in ('нет', 'н', 'no', 'n'):
                print("\nСпасибо за игру! До свидания! 👋")
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    main()
