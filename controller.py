import gui
import db
import comands

def start_phonebook():
    var = comands.start_qгestion()
    if var == 1:
        db.add_contact_to_exel(db.add_contact_to_list(gui.take_contact()))
        print('Контакт добавлен в phonebook.xlsx')
    elif var == 2:
        db.updated_txt_v1(db.read_xlsx())
        print('Файл с контактами создан - phonebook_v1.txt')
    elif var == 3:
        db.updated_txt_v2(db.read_xlsx())
        print('Файл с контактами создан - phonebook_v2.txt')
    elif var == 4:
        db.find_name(input('Введите Имя: '))
