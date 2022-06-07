'''
Данный класс преднозначен для новичков питона,
Которые только начинают брать основы в позновательных целях
Все представленно в виде функций, которые вы легко импортируете к себе на пк
Вначале просто скачиваете нашу библиотеку, потом даете ей название
Например:
    import pstart as pt

Далее через метод pt, обращаетесь ко всем нашим функциям


Распределения будут выглядеть следующим образом

1) Функции с операциями над строками
2) Функции с операциями над числами
3) Фнукции с операциями над списками
4) Функции с операциями над вложенными списками
5) Функции с операциями под словари
6) Функции с операциями под кортежи
7) Сортировки
8) Примеры заданий
'''


# Функции связанные с сортировками

def bubble_sort(arr: list):
    """

    : arr:  list[M]

    """

    # Что делает данная сортировка? Вообще что такое остортировать последовательность?
    # Отсортировать последовательность значит поставить все ее элементы в том или мном порядке
    # В первую очередь вы должны понять что в питоне есть встроенная сортировка arr.sort()
    # Но такие сортировки точно нужно знать. Отсортировать последовательность значит поставить все элементы в порядке
    # Возрастания или убывания - в нашем  случае все будет в порядке возрастания

    arr = [str(x) for x in arr]

    stack = []

    for element in arr:

        if not element.isdigit():

            raise TypeError('Неверный тип данных - скорее всего вы указали какой-то символ внутри строки!')

        else:

            stack += [int(element)]

    try:
        for i in range(len(stack)):

            for j in range(len(stack) - 1):

                if stack[j] > stack[j + 1]:
                    stack[j], stack[j + 1] = stack[j + 1], stack[j]

        return stack

    except:

        raise TypeError('Вы ввели не тот тип данных! - ожидаемо - int')


def insertion_sort(arr: list):
    """

    : arr: type <list>


    Что за сортировка номер 2? Сортировка вставками очень похожа на сортировку пузырьком, по сути это модификация
    Если в случае сортировки пузырьком мы идем по всем элементам в худшем случае n^2 раз, то в данном случае при
    неплохой постановке выборки у нас сортировка будет работать гораздо быстрее чем за n^2 - приблажаясь к O(n)
    смысл заключается в том что мы цепляем элемент и идем не слева направо, а как раз-таки наоборот - справао налево

    """

    arr = [str(x) for x in arr]
    stack = []
    for index in range(len(arr)):

        if not arr[index].isdigit():

            raise TypeError('Скорее всего у вас внутри списка есть строка - проверьте вводимые данные!')
        else:

            stack += [int(arr[index])]

    try:
        for i in range(len(stack)):

            j = i

            while j > 0 and stack[j - 1] > stack[j]:

                if stack[j - 1] > stack[j]:
                    stack[j - 1], stack[j] = stack[j], stack[j - 1]
                j -= 1

    except:

        raise TypeError('Скорее всего ошибка в типе данных')

    return stack


def square_of_digit(digit: int):
    """
    :int digit:
    :return:


    Данный метод выводит квадртаный корень из числа - даже их иррационального
    """

    try:

        return digit ** 0.5

    except:

        raise Exception


def find_multiply_all_digits_list(arr: list):
    """
    :list arr:
    :return:

    Данный метод это замена метода math.prod - мы находим результат умножения всех элементов списка

    """
    arr = [str(x) for x in arr]
    stack = []

    for el in arr:

        if not el.isdigit():

            raise ValueError('В списке различный тип данных')
        else:

            stack += [int(el)]

    result_multiply = 1

    try:

        for el in stack:
            result_multiply *= el

        return result_multiply

    except:

        return Exception


def link_elements_into_one_string(arr: list):
    '''


        arr: <type> list

        Цель: преобразование списка в строку

        Описание: передаем список функции 'link_elements_into_one_string()',
        которая позволяет пройтись по каждому элементу списка
        и вывести каждый элемент в одну строку.
    '''

    result = ''

    try:
        for element in arr:
            result += str(element)

        return result

    except:

        raise Exception


def append_indexies_to_elements_in_list(arr: list):
    """

    :list arr:

    Это очень популярный метод решения задач с учетом вложенных списков
    Например:
        Вам нужно вести учет элементов и их индексов потому что допустим вы потом будете делать определенную перестановку
        и хотите знать предыдущие индексы ваших элементов - для этого стоит знать как реализовывать такой метод


    Стоит учесть что есть и второй вариант реализации этой функции:

    arr = [[x] + arr[x] for x in range(len(arr))] - в нашем случае тоже самое только сделано чуть более понятно

    """

    stack = []

    arr = [str(x) for x in arr]

    for el in arr:

        if not el.isdigit():

            raise ValueError

        else:

            stack += [int(el)]

    result_stack = []

    try:
        for index in range(len(stack)):
            result_stack += [[stack[index]] + [index]]

        return result_stack

    except:

        raise Exception


def sort_double_list_for_the_yours_element(arr: list, index: int):
    """
    :param arr:
    :param index:


    Дання функция принимает 2 значения, вложенный список и индекс по которому будет проходить сортировка вложенного списка
    Например если вам нужно отсортировать уже список списков в котором везде по 2 элемента по первому элементу соответсвенно
    Вначале указываете сам список и потом уже индекс по которому нужно сортировать

    Пример:

        arr = [[1,0], [3,1], [2,2], [1,3]]

        result: [[1,0], [1,3], [2,2], [3,1]

    """

    check_arr = []
    try:

        for stack in arr:
            check_arr += [len(stack)]

        if len(set(check_arr)) != 1:
            raise Exception('В списке не все вложенные списки одного размера')

    except:

        raise Exception('Скорее всего в списке не только тип данных list ')

    try:

        for i in range(len(arr)):

            for j in range(len(arr[i])):
                arr[i][j] = str(arr[i][j])

        stack = []
        for i in range(len(arr)):

            for j in range(len(arr[i])):

                if not arr[i][j].isdigit():

                    raise Exception

                else:

                    arr[i][j] = int(arr[i][j])


    except:

        raise IndexError

    try:
        for el in arr:
            stack += [el]

    except:
        raise Exception

    if not str(index).isdigit():

        raise Exception

    else:
        try:
            for i in range(len(stack)):

                j = i

                while j > 0 and stack[j - 1][index] > stack[j][index]:

                    if stack[j - 1][index] > stack[j][index]:
                        stack[j - 1], stack[j] = stack[j], stack[j - 1]

                    j -= 1

            return stack

        except:

            raise Exception


def serial_number_in_string(string: str, symbol: str):
    '''
        string: <type> str
        symbol: <type> str

        Цель: найти символ (далее - элемент) в строке
        Важно: аргументы (их два), должны передаваться как строка в ''.

        Описание: передаем строке 2 аргумента:
        1. строку, где будет осуществляться поиск элемента;
        2. элемент, который нужно найти.
        Функции serial_number_in_string() позволяет в строке (аргумент 1)
        найти порядковый номер элемента (аргумент 2).
    '''

    counter = 0

    try:
        for i in range(len(string)):

            if string[i] == symbol:
                return i
    except:

        raise Exception

    return None


def quick_sort(arr: list):
    """

    :param arr: <type> list

    Данная функция проводит одну из самых быстрых сортирвоок - сортировка quick_sort
    Она работает еркурсивно здесь самое главное это выбор шага - по моим статистическим примерам самые быстрыя это шаг
    arr / 2, or arr / 3 - доказательство предоставлю ниже


    ЕСЛИ ХОТИТЕ УВИДЕТЬ ПОЧЕМУ ЭТО РАБОТАЕТ БЫСТРО ПРЕДЛАГАЮ ВАМ ВЫЗВАТЬ МЕТОД <check_time_working_quick_sort>
    """

    try:

        if len(arr) < 2:

            return arr

        else:

            element = arr[len(arr) // 2]
            left = [x for x in arr if x < element]
            mid = [x for x in arr if x == element]
            right = [x for x in arr if x > element]

            return quick_sort(left) + mid + quick_sort(right)

    except:

        raise Exception


def check_time_working_quick_sort():
    import random
    """
    
    :param arr: 
    
    Данный метод нужен для того чтобы показать как работает примерно квик сорт на при выборе определенного шага
    
    
    1) Генерируем последовательность на пару тысяч элементов 
    2) Замеряем время квик сорта
    3) Находим наилучший шаг
    4) Делаем сравнение шага 2 и шага 3
    
    Резульат выполнения всего даст нам точное понимание о том какой шаг лучше брать
    Для любознательных советуб выучить не рекурсивные разбиения по типу дейкстры (там много подобных разновидностей)
    """

    generate_stack = []

    for _ in range(2 * 50):
        generate_digit = random.randint(100, 300)

        generate_stack += [generate_digit]

    from datetime import datetime

    start = datetime.now()

    print(f'The list is {generate_stack}')
    print(f'The result is {quick_sort(generate_stack)}')
    print(f'The time is {datetime.now() - start}')
    print('Данная скорость работает на примере шага len(arr) // 2')

    def quick_sort_step_3(arr: list):

        if len(arr) < 2:
            return arr

        else:

            element = arr[len(arr) // 3]

            left = [x for x in arr if x < element]
            mid = [x for x in arr if x == element]
            right = [x for x in arr if x > element]

            return quick_sort_step_3(left) + mid + quick_sort_step_3(right)

    generate_stack = []

    for _ in range(2 * 10 ** 4):
        generate_digit = random.randint(100, 300)

        generate_stack += [generate_digit]

    from datetime import datetime

    start = datetime.now()

    print(f'The list is {generate_stack}')
    print(f'The result is {quick_sort_step_3(generate_stack)}')
    print(f'The time is {datetime.now() - start}')
    print('Данная скорость работает на примере шага len(arr) // 3')

    return 'Как мы видим резульат исполнкния len(arr) // 2 будет больше чем len(arr) // 3'


def convert_string_to_list(string: str):
    '''
        string: <type> str

        Цель: преобразование строки в список
        Важно: аргумент должен передаваться как строка в ''.

        Описание: передаем строку как аргумент функции convert_string_into_list()
        строку, которая позволяет пройтись по каждому элементу строки
        и сформировать список.
    '''
    try:
        res_arr = []

        for i in range(len(string)):
            res_arr += string[i]

        return res_arr

    except:

        raise TypeError


def append_element_to_the_back_of_list(arr: list, element):
    '''

     list: <type> (list)
     element: <type> (str,int,float,list,tuple,dict)
     return: <type> (list)
    '''

    '''
    Цель: добавить элемент в конец списка (далее - элемент)

   Описание: передаем строке 2 аргумента:
    1. исходный список элементов, вводится через пробел;
    2. элемент, который нужно добавить в исходный список(нужно учесть тип вводимого элемента).
    Функции def append() позволяет в список (аргумент 1)
   добавить вводимый с клавиатуры элемент (аргумент 2).
   '''

    try:
        arr += [element]

        return arr

    except:

        raise Exception


def append_element_to_the_front_of_list(arr: list, element):
    """

     arr: <type> (list)
     element: <type> (str,int,float,list,tuple,dict)
     return: <type> (list)

    Цель: добавить элемент в начало списка (далее - элемент)

   Описание: передаем строке 2 аргумента:
    1. исходный список элементов, вводится через пробел;
    2. элемент, который нужно добавить в исходный список(нужно учесть тип вводимого элемента).
    Функции def append() позволяет в список (аргумент 1)
    добавить вводимый с клавиатуры элемент (аргумент 2).


    Коротко говоря мы просто позволяем вам добавить элемент в начало списка а не в конец
    """

    try:

        result = []

        result += [element] + arr

        return result

    except:

        raise Exception


def count_element_in_touple(arr: tuple, element_for_count):
    """
    :<type> arr : tuple:
    :<type> element_for_counts : EACH:
    :return <type> : list:

    Цель данной функции:
        Выводит количество нужного элемента в списке - тот который вы ему зададите

    Реализовано:
        Просто с помощью дополнительной переменной counter, которая считает количество нужного элемента и выводит ее

    """

    if element_for_count not in arr:

        raise Exception

    else:

        try:

            counter = 0

            for element in arr:

                if element == element_for_count:
                    counter += 1

            return counter


        except:

            return Exception


def find_index_of_element_in_tuple(arr: tuple, element):
    """

    :<type> arr : list:
    :<type> element : each:
    :return <type> : list:

    Данная функция возвращает индекс нужного элемента в тапле
    """

    if element not in arr:

        return -1

    else:

        try:

            for i in range(len(arr)):

                if arr[i] == element:
                    return i

            return Exception

        except:

            raise Exception


def find_max_element_in_tuple(arr: tuple):
    """
    :param arr <type> : tuple:
    :return <type> : int:


    Данная функиця возвращает максимальный элемент кортежа - просто путем беребора - бутстрэпа
    """

    try:

        for el in arr:

            if type(el) != int:
                raise Exception

        maximum = arr[0]

        for element in arr:

            if element > maximum:
                maximum = element

        return maximum


    except:

        raise Exception


def find_min_element_of_tuple(arr: tuple):
    """
        :param arr <type> : tuple:
        :return <type> : int:
        Данная функиця возвращает минимальный элемент кортежа - просто путем беребора - бутстрэпа

        Описание: Также подобные 2 метода как макс и мин можно найти в самом питоне - min(tuple), max(tuple)
    """

    try:
        for element in arr:

            if type(element) != int:
                raise Exception

        minimum = arr[0]

        for el in arr:

            if el < minimum:
                minimum = el

        return minimum
    except:

        raise Exception


def max_digit_in_list(arr: list):
    '''
    string: <type> list

    Цель: найти максимальное число в списке
    Важно: в списке не могут находиться буквы, слова и т.п.

    Описание:
    Встроенный Python  max() Функция возвращает максимальный элемент списка
    '''

    if len(arr) == 0:
        raise Exception
    else:
        max_digit = arr[0]

    try:
        for element in arr:

            if element > max_digit:
                max_digit = element

        return max_digit

    except:

        raise Exception


def count_identical_elements_in_string(string: str, element: str):
    '''
    string: <type> str
    element: <type> str

    Цель: найти количество нужного элемента в строке

    Описание: передаем строке 2 аргумента:
    1. строка, где будет осуществлятся поиск и подсчет элемента
    2. элемент, количество которого нужно узнать в строке
    '''
    counter = 0
    try:
        for element in string:

            if element == element:
                counter += 1

        return counter

    except:

        raise Exception


def find_index_of_element_in_list(arr: list, element):
    '''
     arr: <type> (list)
     element: <type> (str,int,float)
     return: <type> (int)
    '''

    ''' 
    Цель: Найти индекс нужного элемента в списке (далее - элемент)

   Описание: передаем строке 2 аргумента:
    1. исходный список элементов, вводится через пробел;
    2. элемент, индекс которого нужно найти в исходном списке элементов (нужно учесть тип вводимого элемента).
    Функция find_index_elements позволяет в списке (аргумент 1)
   нвйти индекс нужного элемента (аргумент 2).
   '''
    try:
        for index in range(len(arr)):

            if element == arr[index]:
                return index


    except:

        raise Exception


def show_all_values_of_dictionary(dictionary: dict):
    """

    :<type> dictionary : dict:
    :return <type> : list:


    Цель данной функции : Выветси все элементы нашего словая в виде списка
    Все сделано обычном бутстрэпом который проходится по ключам словаря и добавляет соответствующие значения в список

    Формат Вывода:

        Список значений
    """

    stack = []

    try:

        for key in dictionary.keys():
            stack += [dictionary[key]]

        return stack

    except:

        raise Exception


def min_digit_in_list(arr: list):
    '''
    string: <type> list

    Цель: найти минимальное число в списке
    Важно: в списке не могут находиться буквы, слова и т.п.

    Описание:
    Встроенный Python  min() Функция возвращает минимальный элемент списка
    '''

    if len(arr) == 0:
        raise Exception
    else:
        min_digit = arr[0]
    try:
        for element in arr:
            if element < min_digit:
                min_digit = element

        return min_digit

    except:
        raise Exception


def find_all_keys_from_dictionary(dictionary: dict):
    """


    :param <type >ictionary : dict:
    :return <list>:

    Функция возвращает все ключи заданного словаря в виде списка

    Решение получено обычном boostrpar
    """

    stack = []

    try:

        for key in dictionary.keys():
            stack += [key]

        return stack

    except:

        raise Exception


def find_if_element_in_dict_values(dictionary: dict, element):
    """

    :param dictionary <type> : dict:
    :param element <type> : each:
    :return True/False, DIGIT - INDEX of the PARE key-value:


    Мы проходимся по всем значения словаря и если встречаем то которое задано, возвразаем True и его индекс

    Решение получение обычным линейный прохождением по всему словарю что позволяет нам спокойно работать за время O(n)
    """

    try:
        counter = 0
        for key in dictionary.keys():

            if dictionary[key] == element:
                return (True, counter)

            counter += 1

        return (False, -1)


    except:

        raise Exception


def index_of_last_find_element(string: str, element: str):
    '''
    string: <type> str
    element: <type> str

    Цель: найти индекс нужного элемента с конца строки
    Важно:
    1. индекс элемента считается с конца строки, т.е. справо налево;
    2. нумерация индексов строки справа налево начивается с -1

    Описание: передаем строке 2 аргумента:
    1. строка, где будет осуществлятся поиск элемента
    2. элемент, индекс которого мы ищем
    '''
    try:
        n = -1
        for e in string:
            n += 1
        string = string[::-1]
        for e in string:
            if e == element:
                return n
            else:
                n -= 1

    except:

        raise Exception


def find_if_element_in_dict_keys(dictionary: dict, element):
    """

    :param dictionary <type> : dict:
    :param element <type> : each:
    :return True/False, DIGIT - INDEX of the PARE key-value:


    Мы проходимся по всем ключам словаря и если встречаем то которое задано, возвразаем True и его индекс

    Решение получение обычным линейный прохождением по всему словарю что позволяет нам спокойно работать за время O(n)
    """

    try:
        counter = 0
        for key in dictionary.keys():

            if key == element:
                return (True, counter)

            counter += 1

        return (False, -1)


    except:

        raise Exception


def index_of_first_find_element_in_str(string: str, symbol: str):
    '''
        string: <type> str
        symbol: <type> str

        Цель: найти индекс первого вхождения элемента
        Важно:
        1. подсчет элементов начинается слева направо;
        2. порядковые номера начинаются с ноля (0) до первого вхождения элемента;

        Описание: передаем строке 2 аргумента:
        1. строка, где будет осуществлятся поиск элемента
        2. элемент, индекс которого мы ищем
        '''
    try:
        i = 0
        counter = 0
        while i < len(string):
            if string[i] == symbol:
                return i
            i += 1
        return -1
    except:
        raise Exception


def remove_last_element_from_list(arr: list):
    """

    :param arr <type> : list:
    :return NOTHING and el:
    """

    try:

        element = arr[-1]

        arr = arr[: len(arr) - 1]

        return arr, element

    except:

        raise Exception


def find_of_last_element_in_str(string: str, symbol: str):
    '''
    string: <type> str
    symbol: <type> str

    Цель: найти индекс нужного элемента с конца строки
    Важно:
    1. индекс элемента считается с конца строки, т.е. справо налево;
    2. нумерация индексов строки справа налево начивается с -1

    Описание: передаем строке 2 аргумента:
    1. строка, где будет осуществлятся поиск элемента
    2. элемент, индекс которого мы ищем
    '''
    try:
        string = string[::-1]
        counter = -1
        for i in range(len(string)):
            if string[i] != symbol:
                counter -= 1
            else:
                return counter

    except:

        raise Exception


def append_new_key_in_dictionary(dictionary : dict, key_v, value):

    """
    :param dictionary <type> dict:
    :param key <type> anyone:
    :param value <type> anyone
    :return <dict>:

    Мы добавим новый ключ к вашему словарю с помощью обычной функции
    """

    try:

        for key in dictionary.keys():

            if key == key_v:
                raise Exception('This key is in dictionary')


        dictionary[key_v] = value
        return dictionary

    except:

        raise Exception


def remove_element_from_list(arr : list, element, equal = False):

    """

    :param arr <type> list:
    :param element <type> anyone:
    :return <list>:

    Мы удалим ваш элемент списка который найдется первым слева направо
    Если передать параметр equal = True, мы удалим все такие элементы

    Алгоритм такой - находим нужный элемент и просто дропаем его с помощью срезов
    """

    try:

        if element not in arr:

            return -1

        if equal == True:

            counter = arr.count(element)

            for i in range(counter):

                arr.remove(element)

            return arr
        else:
            if equal == False:

                arr.remove(element)

                return arr


    except:

        raise Exception


def string_lenth(string: str):


    '''
        string: <type> str

        Цель: вывести длину строки
        Важно: строки вкладываем в кавычки ''

        Описание: передаем аргумент ввиде строки функции string_lenth(),
        которая подсчитывает ее длину.
        '''

    try:
        counter = 0

        for i in range(len(string)):

            counter += 1

        return counter
    except:
        raise Exception
def len_element_in_str(arr : list):
    '''
    string: <type> list

    Цель: найти длину элементов
    Важно: Когда объект является строкой, функция len() возвращает количество символов в строке.

    Описание:
    Функция len() возвращает длину (количество элементов) в объекте
    '''

    try:
        count = 0

        for item in arr:
            count += 1

        return count
    except:

        raise Exception



def remove_all_elements_from_list(arr : list):

    """

    :param arr <type> list:
    :return <list>:

    Цель: Нужно удалить все элементы списка

    Прицнип выполнения: Мы просто пройдемся циклом while и будем удалять элементы пока он не станет пустым
    """

    try:

        while arr:

            arr.pop()

        return arr

    except:

        raise Exception


def append_list_to_the_back_of_list(arr : list, appended : list):

    """

    :param arr <type> list:
    :param appended <type> list:
    :return <type> list:

    Надо вернуть 2 склеенных списка в один
    """


    try:

        result = arr + appended

        return result

    except:

        raise ValueError


def replacing_an_element_in_str(string: str, old: str, new: str):
    '''
    string: <type> str
    old: <type> str
    new: <type> str

    Цель: заменить во всем списке нужный элемент на другой

    Описание: передаем строке 3 аргумента:
    1. строка, где будет осуществлятся замена
    2. элемент, который будем заменять
    3. элемент, на который будем заменять
    '''

    try:
        n = 0
        string2 = ''

        for e in old:

            n += 1

        for e in string:

            if e == old:

                string2 += new

            else:

                string2 += e

        return string2

    except:

        raise Exception






