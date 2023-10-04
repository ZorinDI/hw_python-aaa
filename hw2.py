import csv


def file_opener(file_name = 'D:\Corp_Summary (1).csv'):
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
        print(name, ':', *value)


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

    return reports


def print_report(file_name):
    """ Выводит на экран сводный отчёт по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату"""
    reports = report(file_name)

    for values in reports.values():
        avg = values[4] / values[1]
        print(f'{values[0]}: численность: {values[1]}, вилка: {values[2]} - {values[3]}, средняя зарплата: {avg}')


def saving_with_csv(file_name, new_file_name):
    reports = report(file_name)
    with open(new_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writeheader()
        writer.writerows(reports)



hierarchy('D:\Corp_Summary (1).csv')
print_report('D:\Corp_Summary (1).csv')
