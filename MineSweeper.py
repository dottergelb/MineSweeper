import tkinter, random, tkinter.messagebox, tkinter.simpledialog, webbrowser

window = tkinter.Tk()
window.resizable(False, False)
window.title("Сапер")

rows = 10
cols = 10
mines = 10

field = []
buttons = []

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

gameover = False
customsizes = []


def createMenu():
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=0)
    menusize.add_command(label="Маленький (10x10 с 10 минами)", command=lambda: setSize(10, 10, 10))
    menusize.add_command(label="Средний (20x20 с 40 минами)", command=lambda: setSize(20, 20, 40))
    menusize.add_command(label="Большой (35x35 с 120 минами)", command=lambda: setSize(35, 35, 120))
    menubar.add_command(label="Правила", command=showRules)
    menubar.add_command(label="Ссылка на исходный код", command=showSourceCode)

    menubar.add_cascade(label="Размер", menu=menusize)
    menubar.add_command(label="Выход", command=lambda: window.destroy())
    window.config(menu=menubar)


def setSize(r, c, m):
    global rows, cols, mines
    rows = r
    cols = c
    mines = m
    restartGame()


def prepareGame():
    global rows, cols, mines, field
    field = []
    for x in range(0, rows):
        field.append([])
        for y in range(0, cols):
            #add button and init value for game
            field[x].append(0)
    #generate mines
    for _ in range(0, mines):
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        #prevent spawning mine on top of each other
        while field[x][y] == -1:
            x = random.randint(0, rows - 1)
            y = random.randint(0, cols - 1)
        field[x][y] = -1
        if x != 0:
            if y != 0:
                if field[x - 1][y - 1] != -1:
                    field[x - 1][y - 1] = int(field[x - 1][y - 1]) + 1
            if field[x - 1][y] != -1:
                field[x - 1][y] = int(field[x - 1][y]) + 1
            if y != cols - 1:
                if field[x - 1][y + 1] != -1:
                    field[x - 1][y + 1] = int(field[x - 1][y + 1]) + 1
        if y != 0:
            if field[x][y - 1] != -1:
                field[x][y - 1] = int(field[x][y - 1]) + 1
        if y != cols - 1:
            if field[x][y + 1] != -1:
                field[x][y + 1] = int(field[x][y + 1]) + 1
        if x != rows - 1:
            if y != 0:
                if field[x + 1][y - 1] != -1:
                    field[x + 1][y - 1] = int(field[x + 1][y - 1]) + 1
            if field[x + 1][y] != -1:
                field[x + 1][y] = int(field[x + 1][y]) + 1
            if y != cols - 1:
                if field[x + 1][y + 1] != -1:
                    field[x + 1][y + 1] = int(field[x + 1][y + 1]) + 1


def prepareWindow():
    global rows, cols, buttons
    tkinter.Button(window, text="Начнем сначала?", command=restartGame).grid(row=0, column=0, columnspan=cols,
                                                                             sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
    buttons = []
    for x in range(0, rows):
        buttons.append([])
        for y in range(0, cols):
            b = tkinter.Button(window, text=" ", background='grey', width=4, height=2,
                               command=lambda x=x, y=y: clickOn(x, y))
            b.bind("<Button-3>", lambda e, x=x, y=y: onRightClick(x, y))
            b.grid(row=x + 1, column=y, sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
            b.grid_propagate(True)
            buttons[x].append(b)


def restartGame():
    global gameover
    gameover = False
    for x in window.winfo_children():
        if type(x) != tkinter.Menu:
            x.destroy()
    prepareWindow()
    prepareGame()


def clickOn(x, y):
    global field, buttons, colors, gameover, rows, cols
    if gameover:
        return
    buttons[x][y]["text"] = str(field[x][y])
    if field[x][y] == -1:
        buttons[x][y]["text"] = "☢"
        buttons[x][y].config(background='red', disabledforeground='black')
        gameover = True
        tkinter.messagebox.showinfo("Вот и все...", "Мы никогда не потерпим поражения, пока душа готова побеждать...")
        #now show all other mines
        for _x in range(0, rows):
            for _y in range(cols):
                if field[_x][_y] == -1:
                    buttons[_x][_y]["text"] = "☢"
    else:
        buttons[x][y].config(background='white', disabledforeground=colors[field[x][y]])
    if field[x][y] == 0:
        buttons[x][y]["text"] = " "
        #now repeat for all buttons nearby which are 0... kek
        autoClickOn(x, y)
    buttons[x][y]['state'] = 'disabled'
    buttons[x][y].config(relief=tkinter.SUNKEN)
    checkWin()


def autoClickOn(x, y):
    global field, buttons, colors, rows, cols
    if buttons[x][y]["state"] == "disabled":
        return
    if field[x][y] != 0:
        buttons[x][y]["text"] = str(field[x][y])
    else:
        buttons[x][y]["text"] = " "
    buttons[x][y].config(background='white', disabledforeground=colors[field[x][y]])
    buttons[x][y].config(relief=tkinter.SUNKEN)
    buttons[x][y]['state'] = 'disabled'
    if field[x][y] == 0:
        if x != 0 and y != 0:
            autoClickOn(x - 1, y - 1)
        if x != 0:
            autoClickOn(x - 1, y)
        if x != 0 and y != cols - 1:
            autoClickOn(x - 1, y + 1)
        if y != 0:
            autoClickOn(x, y - 1)
        if y != cols - 1:
            autoClickOn(x, y + 1)
        if x != rows - 1 and y != 0:
            autoClickOn(x + 1, y - 1)
        if x != rows - 1:
            autoClickOn(x + 1, y)
        if x != rows - 1 and y != cols - 1:
            autoClickOn(x + 1, y + 1)


def onRightClick(x, y):
    global buttons
    if gameover:
        return
    if buttons[x][y]["text"] == "☢":
        buttons[x][y]["text"] = " "
        buttons[x][y]["state"] = "normal"
        buttons[x][y].config(background='gray', disabledforeground='black')
    elif buttons[x][y]["text"] == " " and buttons[x][y]["state"] == "normal":
        buttons[x][y]["text"] = "☢"
        buttons[x][y]["state"] = "disabled"
        buttons[x][y].config(background='yellow', disabledforeground='black')


def checkWin():
    global buttons, field, rows, cols
    win = True
    for x in range(0, rows):
        for y in range(0, cols):
            if field[x][y] != -1 and buttons[x][y]["state"] == "normal":
                win = False
    if win:
        tkinter.messagebox.showinfo("Вот и все...", "Побеждают только сильные духом.")


def showRules():
    tkinter.messagebox.showinfo("Правила", "Ваша задача - разминировать поле, на котором расположены мины.\n\n"
                                           "Кликните на клетку, чтобы узнать, что там находится.\n"
                                           "   Если клетка содержит мину, игра заканчивается.\n"
                                           "   Если клетка пустая, то вокруг откроются клетки, которые никак не связаны с минами.\n"
                                           "   Если клетка содержит цифру, то это количество мин, которые находятся вокруг нее. \n\n"
                                           "Левой кнопкой мыши вы можете открывать поля, а правой помечать для себя где находятся мины")


def showSourceCode():
    source_code_url = "https://github.com/dottergelb/MineSweeper"
    webbrowser.open(source_code_url)


createMenu()

prepareWindow()
prepareGame()
window.mainloop()
