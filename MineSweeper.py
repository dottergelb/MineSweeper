import tkinter, random, tkinter.messagebox, tkinter.simpledialog, webbrowser


class MineSweeper:
    def __init__(self, window, size, mines):
        self.window = window
        self.size = size
        self.mines = mines
        self.field = []
        self.buttons = []
        self.colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084',
                       '#000000']
        self.gameover = False
        self.create_menu()
        self.prepare_window()
        self.prepare_game()

    def create_menu(self):
        menubar = tkinter.Menu(self.window)
        menusize = tkinter.Menu(self.window, tearoff=0)
        menusize.add_command(label="Маленький (10x10 с 10 минами)", command=lambda: self.set_size(10,  10))
        menusize.add_command(label="Средний 15x15 с 40 минами)", command=lambda: self.set_size(15,  40))
        menusize.add_command(label="Большой (20x20 с 80 минами)", command=lambda: self.set_size(20,  80))
        menubar.add_cascade(label="Размер", menu=menusize)
        menubar.add_command(label="Правила", command=self.show_rules)
        menubar.add_command(label="Ссылка на исходный код", command=self.show_source_code)
        menubar.add_command(label="Выход", command=self.window.destroy)
        self.window.config(menu=menubar)

    def set_size(self, size, mines):
        self.size = size
        self.mines = mines
        self.restart_game()

    def prepare_game(self):
        self.field = []
        for x in range(0, self.size):
            self.field.append([])
            for y in range(0, self.size):
                self.field[x].append(0)
        # Генерируем мины
        for _ in range(0, self.mines):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            # Проверяем чтобы мина не спавнилась в друг друге
            while self.field[x][y] == -1:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            self.field[x][y] = -1
            self.update_neighbors(x, y)

    def update_neighbors(self, x, y):
        if x != 0:
            if y != 0:
                if self.field[x - 1][y - 1] != -1:
                    self.field[x - 1][y - 1] = int(self.field[x - 1][y - 1]) + 1
            if self.field[x - 1][y] != -1:
                self.field[x - 1][y] = int(self.field[x - 1][y]) + 1
            if y != self.size - 1:
                if self.field[x - 1][y + 1] != -1:
                    self.field[x - 1][y + 1] = int(self.field[x - 1][y + 1]) + 1
        if y != 0:
            if self.field[x][y - 1] != -1:
                self.field[x][y - 1] = int(self.field[x][y - 1]) + 1
        if y != self.size - 1:
            if self.field[x][y + 1] != -1:
                self.field[x][y + 1] = int(self.field[x][y + 1]) + 1
        if x != self.size - 1:
            if y != 0:
                if self.field[x + 1][y - 1] != -1:
                    self.field[x + 1][y - 1] = int(self.field[x + 1][y - 1]) + 1
            if self.field[x + 1][y] != -1:
                self.field[x + 1][y] = int(self.field[x + 1][y]) + 1
            if y != self.size - 1:
                if self.field[x + 1][y + 1] != -1:
                    self.field[x + 1][y + 1] = int(self.field[x + 1][y + 1]) + 1

    def prepare_window(self):
        tkinter.Button(self.window,
                       text="Начнем сначала?",
                       command=self.restart_game).grid(row=0,column=0,columnspan=self.size, sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
        self.buttons = []
        for x in range(0, self.size):
            self.buttons.append([])
            for y in range(0, self.size):
                b = tkinter.Button(self.window, text=" ", background='grey', width=4, height=2,
                                   command=lambda x=x, y=y: self.click_on(x, y))
                b.bind("<Button-3>", lambda e, x=x, y=y: self.on_right_click(x, y))
                b.grid(row=x + 1, column=y, sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
                b.grid_propagate(True)
                self.buttons[x].append(b)

    def restart_game(self):
        self.gameover = False
        for x in self.window.winfo_children():
            if type(x) != tkinter.Menu:
                x.destroy()
        self.prepare_window()
        self.prepare_game()

    def check_win(self):
        win = True
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.field[x][y] != -1 and self.buttons[x][y]['state'] == 'normal':
                    win = False
        if win:
            tkinter.messagebox.showinfo("Вот и все...", "Побеждают только сильные духом.")

    def show_rules(self):
        tkinter.messagebox.showinfo("Правила", "Ваша задача - разминировать поле, на котором расположены мины.\n\n"
                                               "Кликните на клетку, чтобы узнать, что там находится.\n"
                                               "   Если клетка содержит мину, игра заканчивается.\n"
                                               "   Если клетка пустая, то вокруг откроются клетки, которые никак не связаны с минами.\n"
                                               "   Если клетка содержит цифру, то это количество мин, которые находятся вокруг нее. \n\n"
                                               "Левой кнопкой мыши вы можете открывать поля, а правой помечать для себя где находятся мины")

    def show_source_code(self):
        source_code_url = "https://github.com/dottergelb/MineSweeper"
        webbrowser.open(source_code_url)

    def on_right_click(self, x, y):
        ClickGame(self, x, y).on_right_click()

    def click_on(self, x, y):
        ClickGame(self, x, y).click_on()


class ClickGame:
    def __init__(self, mine_sweeper, x, y):
        self.mine_sweeper = mine_sweeper
        self.x = x
        self.y = y

    def click_on(self):
        if self.mine_sweeper.gameover:
            return
        self.mine_sweeper.buttons[self.x][self.y]["text"] = str(self.mine_sweeper.field[self.x][self.y])
        if self.mine_sweeper.field[self.x][self.y] == -1:
            self.mine_sweeper.buttons[self.x][self.y]["text"] = "☢"
            self.mine_sweeper.buttons[self.x][self.y].config(background='red', disabledforeground='black')
            self.mine_sweeper.gameover = True
            tkinter.messagebox.showinfo("Вот и все...",
                                        "Мы никогда не потерпим поражения, пока душа готова побеждать...")
            for _x in range(0, self.mine_sweeper.size):
                for _y in range(0, self.mine_sweeper.size):
                    if self.mine_sweeper.field[_x][_y] == -1:
                        self.mine_sweeper.buttons[_x][_y]["text"] = "☢"
                        self.mine_sweeper.buttons[_x][_y].config(background='red', disabledforeground='black')
        else:
            self.mine_sweeper.buttons[self.x][self.y].config(background='white',
                                                             disabledforeground=self.mine_sweeper.colors[
                                                                 self.mine_sweeper.field[self.x][self.y]])
        if self.mine_sweeper.field[self.x][self.y] == 0:
            self.mine_sweeper.buttons[self.x][self.y]["text"] = " "
            self.auto_click_on()
        self.mine_sweeper.buttons[self.x][self.y]['state'] = 'disabled'
        self.mine_sweeper.buttons[self.x][self.y].config(relief=tkinter.SUNKEN)
        self.mine_sweeper.check_win()

    def auto_click_on(self):
        if self.mine_sweeper.buttons[self.x][self.y]['state'] == 'disabled':
            return
        if self.mine_sweeper.field[self.x][self.y] != 0:
            return
        self.mine_sweeper.buttons[self.x][self.y]["text"] = " "
        self.mine_sweeper.buttons[self.x][self.y].config(background='white',  disabledforeground=self.mine_sweeper.colors[self.mine_sweeper.field[self.x][self.y]])
        self.mine_sweeper.buttons[self.x][self.y]['state'] = 'disabled'
        self.mine_sweeper.buttons[self.x][self.y].config(relief=tkinter.SUNKEN)
        if self.x != 0:
            if self.y != 0:
                self.auto_click_on_recursive(self.x - 1, self.y - 1)
            self.auto_click_on_recursive(self.x - 1, self.y)
            if self.y != self.mine_sweeper.size - 1:
                self.auto_click_on_recursive(self.x - 1, self.y + 1)
        if self.y != 0:
            self.auto_click_on_recursive(self.x, self.y - 1)
        if self.y != self.mine_sweeper.size - 1:
            self.auto_click_on_recursive(self.x, self.y + 1)
        if self.x != self.mine_sweeper.size - 1:
            if self.y != 0:
                self.auto_click_on_recursive(self.x + 1, self.y - 1)
            self.auto_click_on_recursive(self.x + 1, self.y)
            if self.y != self.mine_sweeper.size - 1:
                self.auto_click_on_recursive(self.x + 1, self.y + 1)

    def auto_click_on_recursive(self, x, y):
        self.mine_sweeper.click_on(x, y)

    def on_right_click(self):
        if self.mine_sweeper.gameover:
            return
        if self.mine_sweeper.buttons[self.x][self.y]["text"] == "⚐":
            self.mine_sweeper.buttons[self.x][self.y]["text"] = " "
            self.mine_sweeper.buttons[self.x][self.y]["state"] = "normal"
            self.mine_sweeper.buttons[self.x][self.y].config(background='gray', disabledforeground='black')
        elif self.mine_sweeper.buttons[self.x][self.y]["text"] == " ":
            self.mine_sweeper.buttons[self.x][self.y]["text"] = "⚐"
            self.mine_sweeper.buttons[self.x][self.y]["state"] = "disabled"
            self.mine_sweeper.buttons[self.x][self.y].config(background='yellow', disabledforeground='black')


window = tkinter.Tk()
window.resizable(False, False)
window.title("Сапер")
game = MineSweeper(window, 10, 10)
window.mainloop()
