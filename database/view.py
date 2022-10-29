import itertools
from prettytable import PrettyTable
import model

def print_all(big_data, data):
    table_head = list(big_data[0].keys())
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
        table.add_row(table_data_one[:6])
        table_data_one = table_data_one[6:]
    print(table)  

def print_one(big_data, data):
    table_head = list(big_data[0].keys())
    table_data = []    
    table_data_one = []                                                     
    table_data.append(list(data[0].values()))
    for i in range(len(table_data)):
        table_data_one.append(table_data[i])
    table_data_one = table_data_one[0]
    for i in range(len(table_data_one)):                                                   
        table_data_one[i] = str(table_data_one[i])
    table = PrettyTable(table_head)
    table.add_row(table_data_one)
    print(table)  

def export(data):
    print("Выберите подходящий вариант экспорта данных в файл:\n1. Экспортв оба файла\n\
2. Экспорт в файл CSV\n3. Экспорт в файл JSON\n4. Отмена экспорта данных")
    export_choice = input("Вы выбрали - ")
    while export_choice != '1' and export_choice != '2' and  export_choice != '3' and  export_choice != '4':
        export_choice = input("Введите корректный пункт меню - ")
    if export_choice == '1':
        model.export_csv(data)
        model.export_json(data)
    elif export_choice == '2':
        model.export_csv(data)
    elif export_choice == '3':
        model.export_json(data)
    else:
        print('Вы отменили экспорт данных')
