import Model
import Controller
import View

def menu():
    Controller.read_file()
    print("Выберите необходимый пункт из меню (введите номер пункта):\n1. Показать все имеющиеся заметки\n\
2. Создать новую заметку\n3. Удалить заметку\n4. Редактировать имеющуюся заметку\n5. Найти заметку\n\
6. Завершить работу программы")
    print()
    user_choice = input("Ваш выбор: ")
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4" \
        and user_choice != "5" and user_choice != "6":
        user_choice = input("Необходимо ввести число ( от 1 до 6). Ваш выбор: ")
    if user_choice == "1":
        Model.print_all(Controller.note_book)
        View.menu()
    if user_choice == "2":
        Model.create_note(Controller.note_book)
    if user_choice == "3":
        Model.delete_note(Controller.note_book)
    if user_choice == "4":
        Model.edit_note(Controller.note_book)
    if user_choice == "5":
        Model.search_note(Controller.note_book)
    if user_choice == "6":
        print("До свидания!\n<<<====================================================>>>")
        exit()