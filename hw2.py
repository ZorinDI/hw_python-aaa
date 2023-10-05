def file_opener(file_name):
    """ Открывает файл с информацией, и возвращает строковое представление файла
    без первой строчки(в которой название столбцов)"""
    return open(file_name, 'r').readlines()[1:]


def hierarchy(file_name):
    """Функция получает на вход уже открытый файл, преобразовывает каждую строчку,
    и выводит Департаменты и все его отделы"""
    opened_file = file_opener(file_name)
    departments = {}

    for i in opened_file:
        j = i[1:-2].split(';')

        if j[1] not in departments:
            departments[j[1]] = [j[2]]
        else:
            if j[2] not in departments[j[1]]:
                departments[j[1]].append(j[2])

    for name, value in departments.items():
        print(name, ':', end=' ')
        print(*value, sep=', ')


def report(file_name):
    """Считает для каждого департамента вилку зарплат, количество людей в нём и среднюю зарплату,
    и возвращает словарь с этой информацией"""
    reports = {}
    opened_file = file_opener(file_name)

    for i in opened_file:
        i = i[1:-2].split(';')
        if i[1] not in reports:
            reports[i[1]] = [i[1], 1, float(i[-1]), float(i[-1]), float(i[-1])]
        else:
            reports[i[1]][4] += float(i[-1])
            reports[i[1]][1] += 1
            if reports[i[1]][2] > float(i[-1]):
                reports[i[1]][2] = float(i[-1])
            if reports[i[1]][3] < float(i[-1]):
                reports[i[1]][3] = float(i[-1])
    for keys, values in reports.items():
        reports[keys][4] = values[4] / values[1]

    return reports


def print_report(file_name):
    """ Выводит на экран сводный отчёт по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату"""
    reports = report(file_name)

    for values in reports.values():
        print(f'{values[0]}: численность: {values[1]}, вилка: {values[2]} - {values[3]}, средняя зарплата: {values[4]}')


def saving_with_csv(file_name, new_file_name='new_csv.csv'):
    """Функция, которая записывает в новый csv файл с названием new_file_name
    репорт"""
    reports = report(file_name)
    with open(new_file_name, 'w', newline='') as file:
        for values in reports.values():
            file.write(f'{values[0]}: численность: {values[1]}, вилка:'
                       f' {values[2]} - {values[3]}, средняя зарплата: {values[4]}')
            file.write('\n')


def start_program(file_name, new_file_name='new_csv.csv'):
    """Функция принимает файл, с которым будет работать и просить ввести число, чтобы запустить нужную программу"""
    print('Введите число от 1 до 3 если хотите: \n'
          '1. Вывести иерархию команд \n'
          '2. Вывести сводный отчёт по департаментам \n'
          '3. Сохранить сводный отчёт по департаментам в новый файл.')

    numb = int(input())

    if numb == 1:
        hierarchy(file_name)
    elif numb == 2:
        print_report(file_name)
    elif numb == 3:
        saving_with_csv(file_name, new_file_name)
    else:
        print('Sorry, your number out of range')


# Запускает начало работы
start_program('D:\Corp_Summary (1).csv')

# Я тестировал на файле из степика и всё работало :)
