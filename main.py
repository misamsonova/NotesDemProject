from tkinter import *
from random import choice
from tkinter.ttk import Combobox
from tkinter import messagebox
import os

def username_f():
    f = open("LP.txt", "r")
    k = 0
    name, surname = " ", " "
    for line in f:
        k += 1
        if (k == 1): name = line[:-1];
        if (k == 2): surname = line[0:-1];
        if (k > 2): break;
    f.close()
    username = name + " " + surname
    window(username)
def window(username):
    root2 = Tk()
    root2.title('Личный кабинет')
    root2.geometry('600x300')
    root2.resizable(width=False, height=False)

    lbl_main = Label(root2, text=f'Welcome, {username}.', font=("Arial Bold", 15))
    lbl_main.place(relx=0.5, y=40, anchor=CENTER)

    btn1 = Button(root2, text='Профиль', font=('Calibri', 20, 'bold'),
                  width="17", height ="2", command=lambda:[profile(), root2.withdraw()])
    btn1.place(relx=0.3, y=120, anchor=CENTER)
    btn2 = Button(root2, text='Создание заметки',
                  font=('Calibri', 20, 'bold'), width="17", height ="2", command=lambda:[create_notice(), root2.withdraw()])
    btn2.place(relx=0.73, y=120, anchor=CENTER)
    btn3 = Button(root2, text='Чтение заметок',
                  font=('Calibri', 20, 'bold'), width="17", height ="2", command=lambda:[read_notice(), root2.withdraw()])
    btn3.place(relx=0.3, y=220, anchor=CENTER)
    btn4 = Button(root2, text='Выход', font=('Calibri', 20, 'bold'),
                  width="17", height ="2", command= lambda :[root.deiconify(), root2.destroy()])
    btn4.place(relx=0.73, y=220, anchor=CENTER)

def read_notice():
    rd = Tk()
    rd.title('Заметки.')
    rd.geometry('1000x600')
    rd.resizable(width=True, height=True)

    def find():
        notice.delete('1.0', END)
        f = open("Notices.txt", 'r')
        flag = FALSE
        Title = Ent.get()
        lines = f.readlines()
        num = len(lines)
        for i in range(0, num - 2):
            if (lines[i][:-1] == Title):
                flag = TRUE
                notice.insert('1.0', lines[i+2])
                break
        if (flag==FALSE):
            messagebox.showinfo("Ошибка", "Такой заметки не существует!")
        f.close()


    main = Label(rd, text="Введите название заметки: ", font='Arial 14')
    main.place(relx=0.20, y=40, anchor=CENTER)
    Ent = Entry(rd, font='Arial 13')
    Ent.place(relx=0.5, y=40, anchor=CENTER)
    btn1 = Button(rd, text='Поиск', font=('Calibri', 15, 'bold'), width="14", height="2",
                  command=find)
    btn1.place(relx=0.5, y=100, anchor=CENTER)

    text = Label(rd, text="Текст: ", font='Arial 16')
    text.place(relx=0.5, y=160, anchor=CENTER)
    notice = Text(rd, width=200, height=200, font='Arial 14')
    notice.place(anchor=CENTER)
    notice.pack(side=TOP, pady=[150, 30], padx=20)

    def clear():
        notice.delete('1.0', END)
        Ent.delete(0,END)
    def close_rd():
        rt_d3 = Tk()
        rt_d3.title('Закрытие заметок.')
        rt_d3.geometry('800x200')
        rt_d3.resizable(width=False, height=False)
        lbl = Label(rt_d3, text="Выйти из режима чтения?", font=("Arial Bold", 15))
        lbl.place(relx=0.5, y=40, anchor=CENTER)
        btn1 = Button(rt_d3, text='Да', font=('Calibri', 11, 'bold'), width="14", height="2",
                      command=lambda: [rt_d3.destroy(), rd.destroy(), username_f()])
        btn1.place(relx=0.3, y=120, anchor=CENTER)
        btn2 = Button(rt_d3, text='Нет', font=('Calibri', 11, 'bold'), width="14", height="2",
                      command=lambda: [rt_d3.destroy()])
        btn2.place(relx=0.73, y=120, anchor=CENTER)

    rd.option_add("*tearOff", FALSE)
    main_menu1 = Menu(rd)
    main_menu1.add_cascade(label="Clear all", command=lambda: [clear()])
    main_menu1.add_cascade(label="Close", command=close_rd)
    rd.config(menu=main_menu1)

def profile():
    pr = Tk()
    pr.title('Профиль')
    pr.geometry('350x200')
    pr.resizable(width=False, height=False)

    f = open("LP.txt","r")
    line = f.readlines()
    main = Label(pr, text="Your profile ", font='Arial 18')
    main.place(relx=0.5, y=30, anchor=CENTER)
    e1_0 = Label(pr, text="Name: ", font='Arial 13')
    e1_0.place(relx=0.25, y=70, anchor=CENTER)
    e1 = Label(pr, text = str(line[0]), font='Arial 13')
    e1.place(relx=0.5, y=80, anchor=CENTER)
    e2_0 = Label(pr, text="Surname: ", font='Arial 13')
    e2_0.place(relx=0.20, y=100, anchor=CENTER)
    e2 = Label(pr, text = str(line[1]), font='Arial 13')
    e2.place(relx=0.5, y=110, anchor=CENTER)
    e3_0 = Label(pr, text="Gender: ", font='Arial 13')
    e3_0.place(relx=0.20, y=130, anchor=CENTER)
    e3 = Label(pr, text = str(line[2]), font='Arial 13')
    e3.place(relx=0.5, y=140, anchor=CENTER)
    e4_0 = Label(pr, text="Date of Birth: ", font='Arial 13')
    e4_0.place(relx=0.20, y=170, anchor=CENTER)
    e4 = Label(pr, text = str(line[3]), font='Arial 13')
    e4.place(relx=0.5, y=170, anchor=CENTER)
    f.close()

    def close_pr():
        rt_d2 = Tk()
        rt_d2.title('Закрытие профиля.')
        rt_d2.geometry('800x200')
        rt_d2.resizable(width=False, height=False)
        lbl = Label(rt_d2, text="Выйти из профиля?", font=("Arial Bold", 15))
        lbl.place(relx=0.5, y=40, anchor=CENTER)
        btn1 = Button(rt_d2, text='Да', font=('Calibri', 11, 'bold'), width="14", height="2",
                      command=lambda: [rt_d2.destroy(), pr.destroy(), username_f()])
        btn1.place(relx=0.3, y=120, anchor=CENTER)
        btn2 = Button(rt_d2, text='Нет', font=('Calibri', 11, 'bold'), width="14", height="2",
                      command=lambda: [rt_d2.destroy()])
        btn2.place(relx=0.73, y=120, anchor=CENTER)

    def edit_profile():
        edp = Tk()
        edp.title('Редактирование профиля.')
        edp.geometry('400x250')
        edp.resizable(width=False, height=False)

        main = Label(edp, text="Edit your profile ", font='Arial 18')
        main.place(relx=0.5, y=30, anchor=CENTER)
        e1_0 = Label(edp, text="Name: ", font='Arial 11')
        e1_0.place(relx=0.20, y=80, anchor=CENTER)
        e1_1 = Entry(edp, font='Arial 13')
        e1_1.place(relx=0.5, y=80, anchor=CENTER)
        e2_0 = Label(edp, text="Surname: ", font='Arial 11')
        e2_0.place(relx=0.18, y=110, anchor=CENTER)
        e2_1 = Entry(edp, font='Arial 13')
        e2_1.place(relx=0.5, y=110, anchor=CENTER)
        e3_0 = Label(edp, text="Gender: ", font='Arial 11')
        e3_0.place(relx=0.18, y=140, anchor=CENTER)
        e3_1 = Entry(edp, font='Arial 13')
        e3_1.place(relx=0.5, y=140, anchor=CENTER)
        e4_0 = Label(edp, text="Date of Birth: ", font='Arial 11')
        e4_0.place(relx=0.15, y=170, anchor=CENTER)
        e4_1 = Entry(edp, font='Arial 13')
        e4_1.place(relx=0.5, y=170, anchor=CENTER)

        def write_0():
            f = open("LP.txt", "w")
            Name = e1_1.get()
            for symbol in Name:
                f.write(symbol)
            f.write("\n")
            Surname = e2_1.get()
            for symbol in Surname:
                f.write(symbol)
            f.write("\n")
            Gender = e3_1.get()
            for symbol in Gender:
                f.write(symbol)
            f.write("\n")
            Date = e4_1.get()
            for symbol in Date:
                f.write(symbol)
            f.close()
            edp.destroy()

        btn = Button(edp, text='Сохранить', font=('Calibri', 11, 'bold'), width="10", height="2",
                 command=lambda :[write_0(), profile()])
        btn.place(relx=0.5, y=220, anchor=CENTER)

    pr.option_add("*tearOff", FALSE)
    main_menu1 = Menu(pr)
    main_menu1.add_cascade(label="Edit Profile",
                           command=lambda :[edit_profile(), pr.withdraw()])
    main_menu1.add_cascade(label="Close", command=close_pr)
    pr.config(menu=main_menu1)

def create_notice():
    rt = Tk()
    rt.title('Создание заметки')
    rt.geometry('600x600')
    rt.resizable(width=True, height=True)

    e1_r = Entry(rt, font='Arial 20')
    e1_r.place(relx=0.5, y=60, anchor=CENTER)
    text = Text(rt, width=450, height=450, font='Arial 14')
    text.place(anchor=CENTER)
    text.pack(side=LEFT, pady=[150,30], padx=20)
    combo_r = Combobox(rt)
    combo_r['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    combo_r.current(1)
    combo_r.place(relx=0.5, y=110, anchor=CENTER)

    def info1():
        messagebox.showinfo(title="Информация", message="Ваш файл успешно cохранён!")

    def info2():
        messagebox.showinfo(title="Информация", message="Вы уже сохранили этот файл!")

    def replace():
        f = open("Notices.txt", "r")
        Title = e1_r.get()
        Text = text.get('1.0', END)
        lines = f.readlines()
        num = len(lines)
        for i in range(0, num - 2):
            if (lines[i][:-1] == Title):
                lines[i + 2] = Text
                with open("Notices.txt", 'w') as f:
                    f.writelines(lines)
                break
        f.close()

    def replace_info():
        rpl = Tk()
        rpl.title('Изменение файла.')
        rpl.geometry('400x200')
        rpl.resizable(width=False, height=False)
        lbl = Label(rpl, text="Сохранить файл, учтя изменения?", font=("Arial Bold", 15))
        lbl.place(relx=0.5, y=40, anchor=CENTER)
        btn1 = Button(rpl, text='Да', font=('Calibri', 11, 'bold'), width="10", height="2",
                      command=lambda: [replace(), rpl.destroy()])
        btn1.place(relx=0.3, y=120, anchor=CENTER)
        btn2 = Button(rpl, text='Нет', font=('Calibri', 11, 'bold'), width="10", height="2",
                      command=lambda: [rpl.destroy()])
        btn2.place(relx=0.73, y=120, anchor=CENTER)

    def save_file():
        filename = "Notices.txt"
        if (os.stat(filename).st_size == 0):
            f = open("Notices.txt", "w")
            Title = e1_r.get()
            for symbol in Title:
                f.write(symbol)
            f.write("\n")
            f.write(combo_r.get())
            f.write("\n")
            Text = text.get('1.0', END)
            for symbol in Text:
                f.write(symbol)
            f.write("\n")
            info1()
            f.close()
        else:
            flag = FALSE
            f = open("Notices.txt", "r")
            Title = e1_r.get()
            Text = text.get('1.0', END)
            lines = f.readlines()
            num = len(lines)
            for i in range(0, num-2):
                if (lines[i][:-1] == Title):
                    if(lines[i+2][:]==Text):
                        flag = TRUE
                        info2()
                        break
                if (lines[i][:-1] == Title):
                    f.close()
                    replace_info()
                    break
            if (flag == FALSE):
                f = open("Notices.txt", "r")
                if (Title not in f.read()):
                    f.close()
                    f = open("Notices.txt", "a")
                    Title = e1_r.get()
                    for symbol in Title:
                        f.write(symbol)
                    f.write("\n")
                    f.write(combo_r.get())
                    f.write("\n")
                    Text = text.get('1.0', END)
                    for symbol in Text:
                        f.write(symbol)
                    f.write("\n")
                    info1()
                    f.close()
                f.close()

    def close():
        rt_d = Tk()
        rt_d.title('Закрытие редактора записей.')
        rt_d.geometry('800x200')
        rt_d.resizable(width=False, height=False)
        lbl = Label(rt_d, text="Выйти из редактора?\n (Прежде чем выйти, не забудьте сохранить файл кнопкой Save File)", font=("Arial Bold", 15))
        lbl.place(relx=0.5, y=40, anchor=CENTER)
        btn1 = Button(rt_d, text='Да', font=('Calibri', 11, 'bold'), width="14", height="2",  command=lambda: [rt_d.destroy(), rt.destroy(), username_f()])
        btn1.place(relx=0.3, y=120, anchor=CENTER)
        btn2 = Button(rt_d, text='Нет', font=('Calibri', 11, 'bold'), width="14", height="2",
                      command=lambda: [rt_d.destroy()])
        btn2.place(relx=0.73, y=120, anchor=CENTER)

    def clear():
        text.delete('1.0', END)
        combo_r.current(1)
        e1_r.delete(0, END)

    rt.option_add("*tearOff", FALSE)
    main_menu = Menu(rt)
    main_menu.add_cascade(label="Save File", command = save_file)
    main_menu.add_cascade(label="Close", command = close)
    main_menu.add_cascade(label="Clear all", command = clear)
    rt.config(menu=main_menu)

def window1():
    root3=Tk()
    root3.title('Регистрация')
    root3.geometry('600x500')
    root3.resizable(width=False, height=False)
    lbl_w = Label(root3, text='Пройдите регистрацию:', font=("Arial Bold", 25))
    lbl_w.place(relx=0.5, y=20, anchor=CENTER)

    e1_w = Entry(root3, font='Arial 13')
    e1_w.place(relx=0.5, y=200, anchor=CENTER)
    e2_w = Entry(root3, font='Arial 13')
    e2_w.place(relx=0.5, y=230, anchor=CENTER)
    e3_w = Entry(root3, font='Arial 13')
    e3_w.place(relx=0.5, y=70, anchor=CENTER)
    e4_w = Entry(root3, font='Arial 13')
    e4_w.place(relx=0.5, y=100, anchor=CENTER)
    e5_w = Entry(root3, font='Arial 13')
    e5_w.place(relx=0.5, y=170, anchor=CENTER)

    lbl1_w = Label(root3, text='Придумайте логин:', font=("Arial Bold", 12))
    lbl1_w.place(relx=0.22, y=198, anchor=CENTER)
    lbl2_w = Label(root3, text='Придумайте пароль:', font=("Arial Bold", 12))
    lbl2_w.place(relx=0.21, y=229, anchor=CENTER)
    lbl3_w = Label(root3,
                   text='*Воспользуйтесь генератором паролей,\n написав кол-во символов пароля в окне "Придуймате пароль" и нажав на кнопку "Генерация пароля".',
                 font=("Arial Bold", 9))
    lbl3_w.place(relx=0.5, y=260, anchor=CENTER)
    lbl4_w = Label(root3, text='Укажите своё имя:', font=("Arial Bold", 12))
    lbl4_w.place(relx=0.22, y=68, anchor=CENTER)
    lbl5_w = Label(root3, text='Укажите свою фамилию:', font=("Arial Bold", 12))
    lbl5_w.place(relx=0.18, y=99, anchor=CENTER)
    lbl6_w = Label(root3, text='Ваш пол:', font=("Arial Bold", 12))
    lbl6_w.place(relx=0.28, y=134, anchor=CENTER)
    lbl7_w = Label(root3, text='Дата рождения:', font=("Arial Bold", 12))
    lbl7_w.place(relx=0.24, y=169, anchor=CENTER)

    combo = Combobox(root3)
    combo['values'] = ('Man', 'Woman')
    combo.current(1)
    combo.place(relx=0.5, y=135, anchor=CENTER)

    def randomize():
        lengthPassword = e2_w.get()
        e2_w.delete(0, END)
        for i in range(int(lengthPassword)):
            e2_w.insert(0, choice(alphabet))

    def write():
        f = open("A.txt",'w')
        Login = e1_w.get()
        for symbol in Login:
            f.write(symbol)
        f.write("\n")
        Password = e2_w.get()
        for symbol in Password:
            f.write(symbol)
        f.close()
        f = open("LP.txt", 'w')
        Name = e3_w.get()
        for symbol in Name:
            f.write(symbol)
        f.write("\n")
        Surname = e4_w.get()
        for symbol in Surname:
            f.write(symbol)
        f.write("\n")
        f.write(combo.get())
        f.write("\n")
        DateOfBirth = e5_w.get()
        for symbol in DateOfBirth:
            f.write(symbol)
        f.close()

    btn1_w = Button(root3, text='Зарегистрироваться', font=('Calibri', 16, 'bold'), command= lambda:[write(), root3.destroy()])
    btn1_w.place(relx=0.5, y=330, anchor=CENTER)
    btn2_w = Button(root3, text='Генерация пароля', font=('Calibri', 10, 'bold'), command=randomize)
    btn2_w.place(relx=0.5, y=290, anchor=CENTER)

    alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '-', '.', '@']

root = Tk()
root.title('Авторизация')
root.geometry('600x250')
root.resizable(width = False, height = False)

e1 = Entry(root, font='Arial 13')
e1.place(relx=0.5, y=70, anchor=CENTER)
e2 = Entry(root, font='Arial 13')
e2.place(relx=0.5, y=100, anchor=CENTER)

def read():
    k = 0
    Login = e1.get()
    Password = e2.get()
    f = open("A.txt")
    for line in f:
        if(Login == line[:-1]):k+=1;
        if (Password == line): k+= 1;
    f.close()
    if (k!=2):
        messagebox.showinfo("Ошибка", f'Неверный логин или пароль!');
    else:
        username_f()
        root.withdraw();

btn = Button(root, text='Регистрация', font=('Calibri', 10, 'bold'), command= lambda:[window1()])
btn.place(relx=0.5, y=150, anchor=CENTER)
btn1 = Button(root, text='Войти в личный кабинет', font=('Calibri', 16, 'bold'), command= lambda:[read()])
btn1.place(relx=0.5, y=190, anchor=CENTER)

lbl = Label(root, text='Войдите в личный кабинет:', font=("Arial Bold", 25))
lbl.place(relx=0.5, y=20, anchor=CENTER)
lbl1 = Label(root, text='Логин:', font=("Arial Bold", 15))
lbl1.place(relx=0.25, y=68, anchor=CENTER)
lbl2 = Label(root, text='Пароль:', font=("Arial Bold", 15))
lbl2.place(relx=0.23, y=99, anchor=CENTER)
lbl2 = Label(root, text='*Если вы не зарегистрированы в приложении, нажмите на окно "Регистрация".', font=("Arial Bold", 9))
lbl2.place(relx=0.5, y=120, anchor=CENTER)
root.mainloop()