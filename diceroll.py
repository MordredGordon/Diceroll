from tkinter import *

import dados


def gui():
    types = [4, 6, 8, 10, 12, 20, 100]
    width = 600
    height = 400
    root = Tk()
    root.title("DiceRoll")
    root.iconbitmap('data/favicon.ico')
    root.geometry(str(width)+"x"+str(height))
    root.resizable(False, False)

    tries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    variable = IntVar(root)
    variable.set(tries[0])

    inputFrame = Frame(root)

    triesDropdown = OptionMenu(inputFrame, variable, *tries)

    Lb = Listbox(inputFrame)

    for type in types:
        Lb.insert(type, str(type))

    def roll():
        for i in Lb.curselection():
            global result
            lados = int(Lb.get(i))
            dados.tentativas = variable.get()
            result = dados.rolar(lados)
            showResult.config(text=result)

    btn = Button(inputFrame, text='ROLL!', command=roll)
    frameResult = LabelFrame(root, text="Resultado")
    showResult = Label(frameResult, text="")

    inputFrame.pack()
    inputFrame.place(x=0, height=height, width=200)
    triesDropdown.pack()
    Lb.pack()
    btn.pack()
    frameResult.pack()
    frameResult.place(x=200, height=height, width=width-200)

    showResult.pack()

    root.mainloop()


if(__name__ == "__main__"):
    gui()
