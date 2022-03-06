from tkinter import *

import dados


def gui():
    dices = [4, 6, 8, 10, 12, 20, 100]
    width = 600
    height = 400
    root = Tk()
    root.title("DiceRoll")
    root.iconbitmap('data/favicon.ico')
    root.geometry(str(width)+"x"+str(height))
    root.resizable(False, False)

    tries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    selectedTries = IntVar(root)
    selectedTries.set(tries[0])

    inputFrame = Frame(root)

    triesLabel = Label(inputFrame, text="Nº of dices:")

    triesDropdown = OptionMenu(inputFrame, selectedTries, *tries)

    sidesLabel = Label(inputFrame, text="Size of dices:")

    diceSides = Listbox(inputFrame)

    for dice in dices:
        diceSides.insert(dice, str(dice))

    def roll():
        for i in diceSides.curselection():
            global result
            sides = int(diceSides.get(i))
            rolls = selectedTries.get()
            result = dados.roll(sides, rolls)
            showResult.config(text=result)

    rollButton = Button(inputFrame, text='ROLL!', command=roll)
    frameResult = LabelFrame(root, text="Resultado")
    showResult = Label(frameResult, text="")

    inputFrame.pack()
    inputFrame.place(x=0, height=height, width=200)
    triesLabel.pack()
    triesDropdown.pack()
    sidesLabel.pack()
    diceSides.pack()
    rollButton.pack()
    frameResult.pack()
    frameResult.place(x=200, height=height, width=width-200)

    showResult.pack()

    root.mainloop()


if(__name__ == "__main__"):
    gui()
