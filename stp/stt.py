import datetime
import os
import json
import time
from datetime import date, timedelta

#создает файлы JSON если их нет
def create_json():
    file_path = 'datacontrol.json'
    file_path_2 = 'holidays.json'
    file_path_3 = 'datalog.json'
    # Проверка наличия файла datacontrol.json
    if not os.path.isfile(file_path):
        # Создание нового файла
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл datacontrol.json создан')
    else:
        print('Файл datacontrol.json уже существует')

    # Проверка наличия файла holidays.json
    if not os.path.isfile(file_path_2):
        # Создание нового файла
        data = {}
        with open(file_path_2, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл holidays.json создан')
    else:
        print('Файл holidays.json уже существует')

        # Проверка наличия файла datalog.json
    if not os.path.isfile(file_path_3):
        # Создание нового файла
        data = {}
        with open(file_path_3, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл datalog.json создан')
    else:
        print('Файл datalog.json уже существует')

create_json()


# Получаем текущую дату и время
def date_time_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d %A %H:%M")
    return(formatted_time)

def date_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d")
    return(formatted_time)

#определяет день недели
def day_week_chek():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%A")
    return(formatted_time)


#Запись нового объекта в datacontrol.json
def write_date_control(point):

    # Чтение содержимого файла JSON
    with open('datacontrol.json', 'r') as file:
        data = json.load(file)

    point_add = 9 #сколько очков должно прибавляться в этот день

    # Получаем последнюю дату
    last_date = max(data.keys())

    # Получаем текущую дату
    current_date = datetime.date.today()

    # Проверяем, есть ли пропущенные дни
    if last_date != str(current_date):
        while last_date != str(current_date):

            point_add = 9 #сколько очков должно прибавляться в этот день
            #получаем текущие очки
            last_point = data[last_date]["point"]
            # Увеличиваем дату на 1 день
            last_date = (date.fromisoformat(last_date) + timedelta(days=1)).isoformat()

            # Добавляем пропущенный день с point_add
            data[last_date] = {"point": last_point + -point_add}

    last_point = data[last_date]["point"]
    data[last_date] = {"point": last_point + point}



        # Сохраняем обновленные данные в файл
    with open("datacontrol.json", "w") as file:
        json.dump(data, file, indent=4)


def write_datalog(new_obj):
    # Чтение содержимого файла JSON
    with open('datalog.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data[new_obj['name_obj']] = new_obj
    # Запись обновлённых данных в файл JSON
    with open('datalog.json', 'w') as file:
        json.dump(data, file, indent=4)

#получение последнего номера записи в datalog.json
def number_assignment():
    # Чтение данных из файла JSON
    with open("datalog.json", "r") as file:
        data = json.load(file)

    if data:
        # Поиск максимального значения save_number
        save_number_check = max(obj['save_number'] for obj in data.values())
    else:
        # Обработка случая, когда data пустой
        save_number_check = 0  # Установите значение по умолчанию или обработайте ситуацию соответствующим образом

    return save_number_check

#записывает в файл интервалы каникул
def holidays_write_json(start_date, stop_date):
    # Чтение содержимого файла JSON
    with open('holidays.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data['holidays '+str(start_date) + ' - ' + str(stop_date)] = {'start_date_holidays': str(start_date), 'stop_date_holidays': str(stop_date), 'save_number': 0}
    # Запись обновлённых данных в файл JSON
    with open('holidays.json', 'w') as file:
        json.dump(data, file, indent=4)

# holidays_write_json('nohgfnon', '11')

def calculate_time_difference(start_time, end_time):
    start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %A %H:%M")
    end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %A %H:%M")
    time_difference = end_datetime - start_datetime
    total_minutes = int(time_difference.total_seconds() / 60)
    return total_minutes


def create_nev_log_part_1():
    name_obj = str(number_assignment()+1)
    save_number = number_assignment()+1
    date = date_now()
    day_week = day_week_chek()
    start_time = date_time_now()
    new_obj = {"name_obj": name_obj,
               "save_number": save_number,
               "date": date,
               "day_week": day_week,
               "start_time": start_time}
    print(f'запись {name_obj} создана')
    write_datalog(new_obj)

print(1)

def write_datalog_part_2():
    with open('datalog.json', 'r') as file:
        data = json.load(file)

    save_number = str(number_assignment())

    end_time = date_time_now()
    start_time = data[save_number]['start_time']
    total_time = calculate_time_difference(start_time, end_time)
    factor_point = 1
    points_given = round(total_time // 10 * factor_point)+1000# points give for time


    # Обновляем словарь data с помощью новых значений
    data[save_number]['end_time'] = end_time
    data[save_number]['total_time'] = total_time
    data[save_number]['factor_point'] = factor_point
    data[save_number]['points_given'] = points_given

    # Записываем обновленный словарь data в JSON-файл
    with open('datalog.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f'запись {save_number} закрыта')
    write_date_control(points_given)

create_nev_log_part_1()
time.sleep(2)
write_datalog_part_2()
