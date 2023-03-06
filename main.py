import random

word_fruits = ["Абрикос", "Алыча", "Груша", "Гуава", "Лайм", "Личи", "Манго", "Яблоко"]
word_animals = ["Кот", "Тигр", "Енот", "Волк", "Олень", "Лиса", "Лось", "Заяц"]
word_colors = ["Черный", "Белый", "Синий", "Розовый", "Оранжевый", "Голубой", "Зеленый", "Серый"]

def get_word(words):
    return words[random.randint(0, len(words) - 1)].upper()

def what_type_word():
    print("Выберите категорию загадываемых слов: фрукты/животные/цвета? ")
    type_word = is_valid_type(input().upper())
    return type_word


def is_valid_type(type):
    if type == "ФРУКТЫ" or type == "ЖИВОТНЫЕ" or type == "ЦВЕТА":
        if type == "ФРУКТЫ":
            return word_fruits
        elif type == "ЖИВОТНЫЕ":
            return word_animals
        elif type == "ЦВЕТА":
            return word_colors
    else:
        print("Введена категория отсутствующая в списке. Выберите: фрукты/животные/цвета")
        type = input().upper()
        type = is_valid_type(type)
        return type


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion_list = ['_'] * (len(word) - 2)  # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion_list.insert(0, word[0])
    word_completion_list.append(word[-1])
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    guessed = False # сигнальная метка

    print(display_hangman(tries))
    while tries != 0 and not guessed:
        print("Загаданное слово:", *word_completion_list)
        print("Введите слово или букву: ", end="")
        letter_or_word = input().upper()
        if what_is_input(letter_or_word):
            if letter_or_word in guessed_words:
                print("Такое слово уже называли...")
                continue
            elif letter_or_word == word:
                print("Поздравляем, вы угадали! Загаданное слово:", word)
                guessed = True
            else:
                print("К сожалению, введенное слово неверно...")
                guessed_words.append(letter_or_word)
                tries -= 1
                print(display_hangman(tries))
                continue
        else:
            if letter_or_word in guessed_letters:
                print("Такую букву уже называли...")
                continue
            elif letter_or_word in word:
                print("Поздравляем, данная буква есть в загаданом слове:")
                guessed_letters.append(letter_or_word)
                for i in range(1, len(word) - 1):
                    if letter_or_word == word[i]:
                        word_completion_list[i] = letter_or_word
                if '_' not in word_completion_list:
                    guessed = True
                    print("Поздравляем, вы угадали! Загаданное слово:", word)
            else:
                print("К сожалению, этой буквы в слове нет...")
                guessed_letters.append(letter_or_word)
                tries -= 1
                print(display_hangman(tries))
                continue
    if tries == 0:
        print("К сожалению вам не удалось угадать слово. Повезет в другой раз")





def what_is_input(letter_or_word):
    if len(letter_or_word) > 0 and letter_or_word.isalpha():
        if len(letter_or_word) > 1:
            return True
        else:
            return False
    else:
        print("Введите корректную букву или слово: ", end='')
        letter_or_word = what_is_input(input())
        return letter_or_word




def is_valid_restart(answ):
    if answ == "Y" or answ == "N":
        if answ == "N":
            return False
        else:
            return True
    else:
        print("Введите, пожалуйста, корректный ответ: Y/N")
        answ = is_valid_restart(input().upper())
        return answ



again = True  # сигнальная метка
while again:
    print("Давайте играть в угадайку слов!")
    play(get_word(what_type_word()))
    print("Сыграем еще раз? Y/N")
    is_restart = input().upper()
    again = is_valid_restart(is_restart)
print("Спасибо за интересную игру.")