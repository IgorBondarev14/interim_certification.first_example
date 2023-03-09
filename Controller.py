import View
import json

def start():
    global user_name
    user_name = input("Добрый день. Представьтесь, пожалуйста (Имя будет использовано в поле 'автор'): ")
    print()
    View.menu()

def read_file():
    global note_book
    note_book = []   
    with open('notebook.json', 'r') as fin:
        for row in fin:
            note_book.append(json.loads(row))
    return note_book 

