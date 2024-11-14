def get_words(path):                                    # функция чтения файла со словами
    with open(path,'r',encoding='utf-8') as f:
        return f.read().splitlines()
    
def get_list_of_words(length):                          # функция составления списка слов нужной длины
    list_of_words = get_words(r'C:\Users\polle\Documents\Python\Тинькофф_слова\слова.txt')
    list_of_words = [word.lower() for word in list_of_words if len(word) == length]
    return list_of_words

def search_words(length,user_word):                     # функция поиска подходящих слов
    list_of_words = get_list_of_words(length)
    letters = {ind:user_word[ind] for ind in range(len(user_word)) if user_word[ind].isalpha()}
    possible_words = []
    for word in list_of_words:
        is_break = False
        for key in letters.keys():
            if letters[key] == word[key]:
                continue
            else:
                is_break = True
                break
        if is_break:
            continue
        else:
            possible_words.append(word)
    return possible_words

def shorten_the_list(words):                            # функция сокращения списка слов с использованием доступных букв
    short_list = []
    alphabet = input('Введите буквы, доступные для использования (без пробелов): ').lower()
    for word in words:
        is_break = False
        for letter in word:
            if letter in alphabet:
                continue
            else:
                is_break = True
                break
        if is_break:
            continue
        else:
            short_list.append(word)
    return short_list


                                                       # основная часть программы
print('Вас приветствует программа подбора слов по заданным параметрам')
length = input('Пожалуйста, введите длину слова: ')
while not length.isdigit():
    length = input('Введите цифру: ')
print('Если Вы знаете положение нескольких букв, пожалуйста, введите слово вида **о*о без пробелов:',end=' ')
user_word = input().lower()
words = search_words(int(length),user_word)
print()
print('Список подходящих слов:',*words,sep='\n\t\t\t\t\t\t')
print()
answer = input('Возможно, Вы хотите сократить список слов, указав строку букв, доступных для использования. Ответьте "да" или "нет": ').lower()
while answer != 'да' and answer != 'нет':
        answer = input('да или нет: ').lower()
if answer == 'да':
    short_list = shorten_the_list(words)
    if len(short_list) == 0:
        print('\n\t\t\t\t\t\tК сожалению, я не нашёл подходящих слов...)))')
    else:
        print('Список подходящих слов:',*short_list,sep='\n\t\t\t\t\t\t')