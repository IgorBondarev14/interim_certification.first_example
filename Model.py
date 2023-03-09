import datetime
import json
import Controller
import View
import itertools
from prettytable import PrettyTable

def print_all(data):
    table_head = key_list
    table_data = []
    for i in range(len(data)):                                                          
        table_data.append(list(data[i].values()))
    for i in range(len(table_data)):                                                   
        for j in range(len(table_data[i])):
            table_data[i][j] = str(table_data[i][j])
    table_data_one = []
    for i in range(1, len(table_data)):                                                 
        table_data_one = list(itertools.chain(table_data[0],table_data[i]))
        if i != len(table_data) - 1:
            table_data[0] = table_data_one
    table = PrettyTable(table_head)
    while len(table_data_one) != 0:
        table.add_row(table_data_one[:7])
        table_data_one = table_data_one[7:]
    print(f'{table}\n<<<====================================================>>>')

def print_one(data):
    table_head = key_list
    table_data = []    
    for i in range(len(data)):
        table_data.append(data[i])
    table = PrettyTable(table_head)
    table.add_row(table_data)
    print(f"{table}\n")    

def create_note(data):
    id_list = []
    for i in range(len(data)):
        id_list.append(int(data[i]['id']))
    new_note = []
    print("Для создания записи введите данные")
    print("Создание id. Если хотите, чтобы id заполнился автоматически - введите 'id',\n\
или введите число, для присвоения его в значение id (id не могут повторяться).")
    print(f'Занятые id: {id_list}')
    print("Для отмены создания записи введите Стоп или Stop")
    
    set_id = input("Вы ввели: ")
    if set_id == "Stop" or set_id == "Стоп":
        View.menu()
    if set_id == 'id':
        if len(id_list) < 1:
            set_id = 1
        else:
            set_id = max(id_list) + 1
    else:
        while (set_id.isdigit() == False) or (id_list.count(int(set_id)) > 0) or (int(set_id)) < 1:
            set_id = input("Введите корректное значение, которого нет в списке: ") 
    new_note.append(int(set_id))
    set_name = input("Введите Заголовок: ")
    new_note.append(set_name)
    set_text = input("Введите текст заметки: ")
    new_note.append(set_text)
    today = datetime.datetime.today()
    date_note = today.strftime("%d.%m.%Y")
    new_note.append(date_note)
    time_note = today.strftime("%H.%M.%S")
    new_note.append(time_note)
    new_note.append(Controller.user_name)
    new_note.append("-")
    new_note_dict = dict(zip(key_list, new_note))
    saveble_note = [new_note_dict]
    print(f'id - {set_id}, Заголовок - {set_name},\nТекст - {set_text},\nДата - {date_note}, Время - {time_note}, \
Автор - {Controller.user_name}\n')
    save_answer = input("Хотите сохранить (Да/Нет)? Для сохранения введите 'да', для отмены - введите 'нет': ")
    save_answer = save_answer.lower()
    while save_answer != "да" and save_answer != "нет":
        save_answer = input("Простите, не понял, что Вы ответили. Введите Да или Нет: ")
        save_answer = save_answer.lower()
    if save_answer == "да":
        save_note(saveble_note)
    else:
        print("Изменения не сохранены.")
    print()
    View.menu()

def delete_note(data):
    print_all(Controller.note_book)
    id_list = []
    new_data = []
    for i in range(len(data)):
        id_list.append(str(data[i]['id']))
    choice = str(input("Какую именно запись вы хотите удалить? Введите нужный id(для отмены \
и выхода в меню введите Стоп или Stop): "))
    if choice == "Stop" or choice == "Стоп":
        View.menu()
    while choice not in id_list:
        choice = input("Такой записи нет. Введите корректный id: ") 
    for i in range(len(data)):
        if data[i]["id"] != int(choice):
            new_data.append(data[i])
    resave_note(new_data)
    print("Запись удалена")
    print()
    View.menu()

def edit_note(data):
    print_all(Controller.note_book)
    id_list = []
    for i in range(len(data)):
        id_list.append(str(data[i]['id']))
    print(id_list)
    choice = str(input("Какую именно запись вы хотите изменить? Введите нужный id (для отмены \
и выхода в меню введите Стоп или Stop): "))
    if choice == "Stop" or choice == "Стоп":
        View.menu()
    while choice not in id_list:
        choice = input("Такой записи нет. Введите корректный id: ")  
    edit_choice = input("Что вы хотите изменить в записи (Выберите подходящий пункт):\n1. Заголовок\n2. Текст\n3. Заголовок и Текст\
    \n4. Ничего (отмена)\nВы выбрали: ")
    while edit_choice != "1" and edit_choice != "2" and edit_choice != "3" and edit_choice != "4":
        edit_choice = input("Введите номер необходимого пункта: ")
    if edit_choice == "1":
        new_name = input("Введите новый Заголовок: ")
        data[int(choice)-1]["Заголовок"] = new_name
        mandatory_change(data, choice)
        resave_note(data)
    if edit_choice == "2":
        new_text = input("Введите новый Текст: ")
        data[int(choice)-1]["Текст"] = new_text
        mandatory_change(data, choice)
        resave_note(data) 
    if edit_choice == "3":
        new_name = input("Введите новый Заголовок: ")
        new_text = input("Введите новый Текст: ")
        data[int(choice)-1]["Заголовок"] = new_name
        data[int(choice)-1]["Текст"] = new_text
        mandatory_change(data, choice)
        resave_note(data) 
    if edit_choice == "4":
        print("Вы отменили изменение")
    View.menu()

def search_note(data):
    search_data = []
    name_list = []
    choice = str(input("Выберите критерий поиска:\n1. Поиск по критерию\n2. Поиск по содержанию\n\
3. Ничего не искать (выйти в меню)\nВы выбрали: "))
    while choice not in ("1", "2", "3"):
        choice = str(input("Введите нужный номер (1, 2 или 3): "))
    if choice == "1":
        choice_criteria = str(input("Выберите критерий отбора:\n1. id\n2. Заголовок\n3. Текст\n4. Дата\n5. Время\
\n6. Автор\n7. Вернутся в основное меню\nВы выбрали: "))
        while choice_criteria not in ("1", "2", "3", "4", "5", "6", "7"):
            choice_criteria = str(input("Вы ввели не существующий пункт меню. Выберите корректный: "))
        if choice_criteria == "1":
            id_list = []
            for i in range(len(data)):
                id_list.append(str(data[i]['id']))
            print(id_list)
            criteria = str(input("Введите нужный id: "))
            while criteria not in id_list:
                criteria = str(input("Введите существующий id: "))
            for i in range(len(data)):
                if data[i]["id"] == int(criteria):
                    search_data=(list(data[i].values()))
            print_one(search_data)
        if choice_criteria == "2":
            for i in range(len(data)):
                name_list.append(str(data[i]['Заголовок']))
            print(name_list)
            criteria = str(input("Введите нужный Заголовок: "))
            while criteria not in name_list:
                criteria = str(input("Введите существующий Заголовок: "))
            for i in range(len(data)):
                if data[i]["Заголовок"] == criteria:
                    search_data.append(data[i])
            print_all(search_data)
        if choice_criteria == "3":
            for i in range(len(data)):
                name_list.append(str(data[i]['Текст']))
            print(name_list)
            criteria = str(input("Введите нужный Текст: "))
            while criteria not in name_list:
                criteria = str(input("Введите существующий Текст: "))
            for i in range(len(data)):
                if data[i]["Текст"] == criteria:
                    search_data.append(data[i])
            print_all(search_data)
        if choice_criteria == "4":
            for i in range(len(data)):
                name_list.append(str(data[i]['Дата']))
            print(name_list)
            criteria = str(input("Введите нужную Дата: "))
            while criteria not in name_list:
                criteria = str(input("Введите существующую Дата: "))
            for i in range(len(data)):
                if data[i]["Дата"] == criteria:
                    search_data.append(data[i])
            print_all(search_data)        
        if choice_criteria == "5":
            for i in range(len(data)):
                name_list.append(str(data[i]['Время']))
            print(name_list)
            criteria = str(input("Введите нужную Время: "))
            while criteria not in name_list:
                criteria = str(input("Введите существующую Время: "))
            for i in range(len(data)):
                if data[i]["Время"] == criteria:
                    search_data.append(data[i])
            print_all(search_data) 
        if choice_criteria == "6":
            for i in range(len(data)):
                if data[i]['Автор'] not in name_list:
                    name_list.append(str(data[i]['Автор']))
            for i in range(len(data)):
                if data[i]['Редактировал'] != "-" and data[i]['Редактировал'] not in name_list:
                    name_list.append(str(data[i]['Редактировал']))
            print(name_list)
            criteria = str(input("Введите нужного Автора: "))
            while criteria not in name_list:
                criteria = str(input("Введите существующего Автора: "))
            for i in range(len(data)):
                if data[i]["Автор"] == criteria:
                    search_data.append(data[i])
                if data[i]["Редактировал"] == criteria:
                    search_data.append(data[i])
            print_all(search_data)
    if choice == "2":
        criteria = input("Введите текст или символы для поиска (для отмены и выхода в меню введите Стоп или Stop): ")
        if criteria == "Stop" or choice == "Стоп":
            View.menu()   
        for i in range(len(data)):
            for key in key_list:
                if str(data[i][key]).count(criteria) > 0:
                    search_data.append(data[i])
                    break
        print_all(search_data)
    View.menu()

def save_note(data):
    with open('notebook.json', 'a', encoding = 'utf-8') as list_json:
        for i in range(len(data)):
            json.dump(data[i], list_json)
            list_json.write('\n')
    list_json.close
    print("Запись сохранена")

def resave_note(data):
    with open('notebook.json', 'w', encoding = 'utf-8') as list_json:
        for i in range(len(data)):
            json.dump(data[i], list_json)
            list_json.write('\n')
    list_json.close

def mandatory_change(data, index):
    today = datetime.datetime.today()
    data[int(index)-1]["Дата"] = today.strftime("%d.%m.%Y")
    data[int(index)-1]["Время"] = today.strftime("%H.%M.%S")
    data[int(index)-1]["Редактировал"] = Controller.user_name

global key_list
key_list = ["id", "Заголовок", "Текст", "Дата", "Время", "Автор", "Редактировал"]