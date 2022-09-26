import gui
import dp
import comands

def start_phonebook():
    var = comands.start_qгestion()
    if var == 1:
        dp.add_contact_to_exel(dp.add_contact_to_list(gui.take_contact()))
        print('Контакт добавлен в phonebook.xlsx')
    elif var == 2:
        dp.updated_txt_v1(dp.read_xlsx())
        print('Файл с контактами создан - phonebook_v1.txt')
    elif var == 3:
        dp.updated_txt_v2(dp.read_xlsx())
        print('Файл с контактами создан - phonebook_v2.txt')
    elif var == 4:
        dp.find_name(input('Введите Имя: '))
