import csv
import json
import view

def choice_file():
    global employee
    global user_choice
    print("Выберите файл для обработки:\n1. database.csv\n2. database.json")
    user_choice = input("Выберите номер пункта меню: ")
    while user_choice != '1' and user_choice != '2':
        user_choice = input("Введите корректный номер пункта меню: ")
    user_choice = int(user_choice)
    if user_choice == 1:
        employee = read_csv()
    elif user_choice == 2:
        employee = read_json()
    return employee

def read_csv():
    global employee
    employee = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee

def read_json():
    global employee
    employee = []    
    with open('database02.json', 'r') as fin:
        for row in fin:
            employee.append(json.loads(row))
    return employee        

def choice_action():
    print("\n" + "=" * 50)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников")
    print("3. Добавить сотрудника")
    print("4. Удалить сотрудника")
    print("5. Обновить данные сотрудника")
    print("6. Экспортировать данные в файл")
    print("7. Показать всю таблицу")
    print("8. Закончить работу")
    user_act_choice = input("Введите номер необходимого действия: ")
    while user_act_choice != '1' and user_act_choice != '2' and user_act_choice != '3' and user_act_choice != '4' \
        and user_act_choice != '5' and user_act_choice != '6' and user_act_choice != '7' and user_act_choice != '8':
        user_act_choice = input("Введите номер действия, в пределах от 1 до 8: ")
    if user_act_choice == '1':
        search(list(employee))
    elif user_act_choice == '2':
        selection(employee)
    elif user_act_choice == '3':
        create(employee)
    elif user_act_choice == '4':   
        delete(employee)
    elif user_act_choice == '5':
        edit(employee)
    elif user_act_choice == '6':
        view.export(employee)
        choice_action()
    elif user_act_choice == '7':
        view.print_all(employee, employee)
        choice_action()
    else: 
        print("Работа завершена")

def search(data):
    global employee
    print("Выберете параметр поиска:\n1. Фамилия\n2. Имя\n3. Должность\n4. Телефон\n5. Зарплата")
    search_choice = input("Вы выбрали - ")
    while search_choice != '1' and search_choice != '2' and search_choice != '3' \
        and search_choice != '4' and search_choice != '5':
        search_choice = input("Введите корректный номер пункта ")
    search_choice = int(search_choice)
    if search_choice == 1:
        search_choice = 'last_name'
        search_query = input('Введите поисковый запрос - ')
    elif search_choice == 2:
        search_choice = 'first_name'
        search_query = input('Введите поисковый запрос - ')
    elif search_choice == 3:
        search_choice = 'position'
        search_query = input('Введите поисковый запрос - ')
    elif search_choice == 4:
        search_choice = 'phone_number'
        search_query = input('Введите поисковый запрос - ')
    elif search_choice == 5:
        search_choice = 'salary' 
        search_query = float(input('Введите поисковый запрос - ')   )
    search_count = 0
    print('Результаты поиска:')

    table_data = []
    for i in range(len(data)):
        if data[i][search_choice] == search_query:
            table_data.append(data[i])
            search_count += 1
    if search_count == 1:
        view.print_one(employee, table_data)
    elif search_count != 0:
        view.print_all(employee, table_data)
    if search_count == 0: 
        print("Ничего не найдено")
    choice_action()

def selection(data):
    print("Выберите нужный вариант отбора:\n1. Должность\n2. Заработная плата")
    selection_choice = input("Вы выбрали - ")
    while selection_choice != '1' and selection_choice != '2':
        selection_choice = input("Введите корректный номер пункта ")
    selection_choice = int(selection_choice)
    selection_count = 0
    table_data = []
    if selection_choice == 1:
        for i in range(len(data)):
            print(f"{i + 1}. {data[i]['position']}")
        print("Введите номер должности для выбора всех сотрудников этой должности")
        selection_position = int(input("Вы выбрали - "))
        while selection_position < 1 or selection_choice > len(data):
            selection_position = int(input("Введите корректный номер пункта - "))
        for i in range(len(data)):
            if data[i]['position'] == data[selection_position - 1]['position']:
                table_data.append(data[i])
                selection_count += 1
        if selection_count == 1:
            view.print_one(employee, table_data)
        elif selection_count != 0:
            view.print_all(employee, table_data)
        else:
            print("Упс. Сотрудников с выбранной должностью нет.")
    else:  
        print("Введите начальный размер заработной платы для выборки")
        min_selection_salary = float(input("Вы ввели - "))
        print("Введите конечный размер заработной платы для выборки")
        max_selection_salary = float(input("Вы ввели - "))
        selection_count = 0
        for i in range(len(data)):
            if min_selection_salary < data[i]['salary'] < max_selection_salary:
                table_data.append(data[i])
                selection_count += 1
        if selection_count == 1:
            view.print_one(employee, table_data)
        elif selection_count > 1:
            view.print_all(employee, table_data)
        elif selection_count == 0:
            print("Сотрудников в выбранной 'вилке зарплат' не найдено" )   
    choice_action()
   
def create(data):
    id_list = []
    for i in range(len(data)):
        id_list.append(data[i]['id'])
    new_entry = []
    print("Для создания записи введите данные")
    print("Создание id. Если хотите, чтобы id заполнился автоматически - введите 'id',\n\
или введите число, для присвоения его в значение id.")
    print(f'Занятые id: {id_list}')
    
    set_id = input("Вы ввели - ")
    if set_id == 'id':
        set_id = max(id_list) + 1
    else:
        while set_id.isdigit() == False:
            set_id = input("Введите корректное значение - ") 

    new_entry.append(set_id)
    set_last_name = input("Введите фамилию - ")
    new_entry.append(set_last_name)
    set_first_name = input("Введите имя - ")
    new_entry.append(set_first_name)
    set_position = input("Введите должность - ")
    new_entry.append(set_position)
    set_phone_number = input("Введите номер телефона - ")
    while set_phone_number.isdigit() == False:
            set_phone_number = input("Введите корректное значение - ")
    new_entry.append(set_phone_number)
    set_salary = input("Введите зарплату - ")
    while set_salary.isdigit() == False:
        set_salary = input("Введите корректное значение - ")
    set_salary = float(set_salary)
    new_entry.append(set_salary)
    keys_list = list(data[0].keys())
    new_empl_dict = dict(zip(keys_list, new_entry))
    new_employee =[new_empl_dict]
    employee.append(new_empl_dict)
    print(f'Новый сотрудник:\n')
    view.print_one(employee, new_employee)
    
    print("Хотите сохранить внесенные данные в файл?\nВыберете подходящий пункт меню:\n1. Да\n2. Нет")
    export_choice = input("Вы выбрали - ")
    while export_choice != '1' and export_choice != '2':
        export_choice = input("Выберите корректный номер пункта меню: ")
    if export_choice == '1':
        view.export(employee)
    else:
        print("Изменения не сохранены.")
    choice_action()  
  
def delete(data):
    id_list = []
    for i in range(len(data)):
        id_list.append(data[i]['id'])
    print('Выберите сотрудника для удаления:')
    view.print_all(data, data)
    print("Введите id сотрудника для удаления")
    deleted_id = input("Вы ввели - ")
    while deleted_id.isdigit() == False:
        deleted_id = input("Введите корректный id - ")
        while deleted_id not in id_list:
            deleted_id = input("Введите корректный id из списка выше - ") 
    deleted_id = int(deleted_id)
    for i in range(len(data)):
        if data[i]['id'] == deleted_id:
            data.pop(i)  
    view.print_all(data, data)
    print("Для подтверждения удаления - сделайте экспорт данных в файл")
    view.export(data)
    choice_action()
   
def edit(data):
    id_list = list(data[0].keys())
    print('Выберите сотрудника для редактирования:')
    view.print_all(data, data)
    print("Введите id сотрудника для редактирования")
    edit_id = input("Вы ввели - ")
    while edit_id.isdigit() == False:
        edit_id = input("Введите корректный id - ")
        while edit_id not in id_list:
            edit_id = input("Введите корректный id из списка выше - ") 
    edit_id = int(edit_id)
    print("Какой раздел вы хотите изменить?")
    print("1. id\n2. Фамилия\n3. Имя\n4. Телефон\n5. Должность\n6. Зарплата")
    search_choice = input("Вы выбрали - ")
    while search_choice != '1' and search_choice != '2' and search_choice != '3' \
        and search_choice != '4' and search_choice != '5' and search_choice != '6':
        search_choice = input("Введите корректный номер пункта ")
    search_choice = int(search_choice)
    if search_choice == 1:
        search_choice = 'id'
    elif search_choice == 2:
        search_choice = 'last_name'
    elif search_choice == 3:
        search_choice = 'first_name'
    elif search_choice == 4:
        search_choice = 'position'
    elif search_choice == 5:
        search_choice = 'phone_number'
    elif search_choice == 6:
        search_choice = 'salary'
    if search_choice == 'id':
        data[edit_id - 1][search_choice] = int(input("Введите новое значение - "))
    elif search_choice == 'salary':
        data[edit_id - 1][search_choice] = float(input("Введите новое значение - "))
    else:
        data[edit_id - 1][search_choice] = input("Введите новое значение - ")
    print(f"Измененные данные:\n")
    view.print_all(data, data)
    print("Для подтверждения изменений - сделайте экспорт данных в файл\n")
    view.export(data)
    choice_action()
 
def export_csv(data):
    with open('database.csv', 'w', encoding = 'utf-8') as ex_li_csv:
        for i in range(len(data)):
            new_list = []
            new_string = ''
            new_list.append(list(data[i].values()))  
            for j in range(len(new_list)):
                new_string = ','.join(map(str, new_list[j]))
            ex_li_csv.write(str(new_string))
            ex_li_csv.write('\n')
    ex_li_csv.close()
    print("Экспорт в файл database.csv завершен")

def export_json(data):
    with open('database02.json', 'w', encoding = 'utf-8') as ex_li_json:
        for i in range(len(data)):
            json.dump(data[i], ex_li_json)
            ex_li_json.write('\n')
    ex_li_json.close
    print("Экспорт в файл database.json завершен")
