import tkinter as tk

def take_contact():
    name = input('Enter Name: ')
    sname = input('Enter Surname: ')
    tp_num= input('Enter telephone number: ')
    description = input('Enter description: ')
    return [name, sname, tp_num, description]

# def window():
#     window = tk.Tk() 
#     window.title("PhoneBook") 
#     window.geometry("600x500+500+200")
#     window.resizable(False, False)
#     window.config(bg="#fff2e6")
#     label1 = tk.Label(window, text="pHONE bOOK 2000",
#                 font=('Times New Roman', 20, 'bold'),
#                 fg="blue",
#                 bg="#fff2e6")
#     label1.pack()
#     btn1 = tk.Button(window, text=f"Start",
#                  font=('Courier New', 12, 'bold'),
#                 fg="#ff9933",
#                 bg="#ffe6cc",
#                 height=1,
#                 width=8,
#                 command=minus) 
#     btn1.pack()

#     window.mainloop()